# coding:utf-8
from icssploit.clients.s7_client import S7Client
from icssploit.protocols.s7comm import *
from icssploit.protocols.cotp import *
from scapy.supersocket import StreamSocket
from scapy.fields import *
import socket
import struct
import binascii


class MyS7Client(S7Client):
    def __init__(self, callingMaxAmQ, calledMaxAmQ, name, ip, port=102, src_tsap='\x01\x00', rack=0, slot=2, timeout=2):
        super(MyS7Client, self).__init__(name, ip, port, src_tsap, rack, slot, timeout)
        
        # Connect MaxAmQ setting
        self.struct = struct.Struct('!H')
        self.callingMaxAmQ = callingMaxAmQ
        self.calledMaxAmQ = calledMaxAmQ
        self.notResponsePackets = []


    def connect(self):
        sock = socket.socket()
        sock.settimeout(self._timeout)
        sock.connect((self._ip, self._port))
        self._connection = StreamSocket(sock, Raw)
        packet1 = TPKT() / COTPCR()
        packet1.Parameters = [COTPOption() for i in range(3)]
        packet1.PDUType = "CR"
        packet1.Parameters[0].ParameterCode = "tpdu-size"
        packet1.Parameters[0].Parameter = "\x0a"
        packet1.Parameters[1].ParameterCode = "src-tsap"
        packet1.Parameters[2].ParameterCode = "dst-tsap"
        packet1.Parameters[1].Parameter = self._src_tsap
        packet1.Parameters[2].Parameter = self._dst_tsap
        self.send_receive_packet(packet1)
        packet2 = TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="Job",
                                                    Parameters=S7SetConParameter(MaxAmQcalling=self.calledMaxAmQ,
                                                                                 MaxAmQcalled=self.calledMaxAmQ))
        rsp2 = self.send_receive_s7_packet(packet2)
        if rsp2:
            self._connected = True
        # Todo: Need get pdu length from rsp2


    def close(self):
        self._connection.close()

    def send_s7_packet(self, packet):
        if self._connection:
            packet = self._fix_pdur(packet)

            # add not response packet
            pdur = packet.payload.payload.PDUR
            if pdur in notResponsePackets:
                client.logger.error("<send_s7_packet error>:PDUr correspond is already in NotResponsePackets!")
            else:
                notResponsePackets.append(pdur)
            # send packet
            try:
                self._connection.send(packet)

            except Exception as err:
                self.logger.error(err)
                return None

        else:
            self.logger.error("Please create connect before send packet!")


    def receive_s7_packet(self):
        if self._connection:
            try:
                rsp = self._connection.recv()
                if rsp:
                    rsp = TPKT(str(rsp))

                    # delete received pdur correspond NotResponsePackets
                    if pdur in self.notResponsePackets:
                        pdur = rsp.payload.payload.PDUR
                        self.notResponsePackets.remove(pdur)
                    else:
                        self.logger.error("<receive_s7_packet error>PDUr is not in NotResponsePackets!")
                
                return rsp

            except Exception as err:
                self.logger.error(err)
                return None
        else:
            self.logger.error("Please create connect before receive packet!")


    
    def getReadVarPacket(self, items):
        read_items = []
        items_data = []

        if isinstance(items, list):
            for i in range(len(items)):
                try:
                    transport_size, block_num, area_type, address = self.get_item_pram_from_item(items[i])
                    length = int(items[i][3])
                    if transport_size:
                        read_items.append(S7ReadVarItemsReq(TransportSize=transport_size,
                                                            GetLength=length,
                                                            BlockNum=block_num,
                                                            AREAType=area_type,
                                                            Address=address
                                                            )
                                          )
                except Exception as err:
                    self.logger.error("Can't create read var packet because of: \r %s" % err)
                    return None
        else:
            self.logger.error("items is not list please check again")
            return None

        return TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="Job", 
                                                 Parameters=S7ReadVarParameterReq(Items=read_items))



