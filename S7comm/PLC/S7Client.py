from struct import pack
import time
from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *
from scapy.supersocket import StreamSocket
import socket
from baseClass import Base
from scapy.compat import raw

class MyS7Client(Base):
    
    def __init__(self, name, ip, port=102, src_tsap='\x01\x00', rack=0, slot=2, timeout=2):
        '''

        :param name: Name of this targets
        :param ip: S7 PLC ip
        :param port: S7 PLC port (default: 102)
        :param src_tsap: src_tsap
        :param rack: cpu rack (default: 0)
        :param slot: cpu slot (default: 2)
        :param timeout: timeout of socket (default: 2)
        '''
        super(MyS7Client, self).__init__()
        self._ip = ip
        self._port = port
        self._slot = slot
        self._src_tsap = src_tsap
        self._dst_tsap = "\x01".encode() + struct.pack('B', rack * 0x20 + slot)
        self._pdur = 1
        self.protect_level = None
        self._connection = None
        self._connected = False
        self._timeout = timeout
        self._pdu_length = 480
        self.readable = False
        self.writeable = False
        self.authorized = False
        self._password = None
        self._mmc_password = None
        self.is_running = False

        self.pktCounts = 0


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


        packet = TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="Job", 
                                                    Parameters=S7SetConParameter(MaxAmQcalling=0x000A, 
                                                                                 MaxAmQcalled=0x000A,
                                                                                 PDULength = 0x00f0))



        rsp2 = self.send_receive_s7_packet(packet)
        if rsp2:
            self._connected = True
        # Todo: Need get pdu length from rsp2


    def send_receive_packet(self, packet):
        if self._connection:
            try:
                rsp = self._connection.sr1(packet, timeout=self._timeout)
                return rsp

            except Exception as err:
                self.logger.error(err)
                return None

        else:
            self.logger.error("Please create connect before send packet!")

    def send_receive_s7_packet(self, packet):
        if self._connection:
            packet = self._fix_pdur(packet)
            try:
                rsp = self._connection.sr1(packet, timeout=self._timeout)
                msg = "[request]" + raw(packet).hex()
                self.logger.info(msg)
                if rsp:
                    rsp = TPKT(raw(rsp))
                    msg = "[responde]" + raw(rsp).hex()
                    self.logger.info(msg)
                return rsp

            except Exception as err:
                self.logger.error(err)
                return None

        else:
            self.logger.error("Please create connect before send packet!")


    def send_s7_packet(self, packet):
        if self._connection:
            packet = self._fix_pdur(packet)
            try:
                self._connection.send(packet)
                self.pktCounts = self.pktCounts + 1
                msg ="[request]" + raw(packet).hex()
                self.logger.info(msg)
            except Exception as err:
                self.logger.error(err)
                return None
        else:
            self.logger.error("Please create connect before send packet!")

    def _fix_pdur(self, payload):
        if self._pdur > 65535:
            self._pdur = 1
        try:
            payload.PDUR = self._pdur
            self._pdur += 1
            return payload
        except Exception as err:
            self.logger.error(err)
            return payload


target = MyS7Client(name="test", ip="192.168.178.21", rack=0, slot=1)

target.connect()

a = input("continue")

packet = TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="Job", Parameters=S7SetConParameter())
             
target.send_s7_packet(packet)
