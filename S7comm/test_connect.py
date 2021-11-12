# coding:utf-8

from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *
from scapy.supersocket import StreamSocket
import socket
from icssploit.clients.s7_client import S7Client
from scapy.compat import raw
from scapy.all import sniff
import threading

class MyS7Client(S7Client):
    
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
        super(MyS7Client, self).__init__(name, ip, port, src_tsap, rack, slot, timeout)
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

    def send_s7_packet(self, packet):
        if self._connection:
            packet = self._fix_pdur(packet)
            try:
                self._connection.send(packet)
                self.pktCounts = self.pktCounts + 1
                msg = "[Packet Number:" + str(self.pktCounts) + "]\n"
                msg = msg + "          [Time:" + time.strftime("%H:%M:%S" , time.localtime()) + "]\n"
                msg = msg + "          [Content: " + self.packetStr_to_hex(raw(packet)) + "]\n"
                self.logger.info(msg)
            except Exception as err:
                self.logger.error(err)
                return None
        else:
            self.logger.error("Please create connect before send packet!")
    
    def packetStr_to_hex(self, packetStr):
        str = ""
        for c in packetStr:
            str = str + c.encode('hex')
        return str


    def receive(self):
        while( True):
            pkts = sniff(opened_socket=self._connection,prn = lambda pkt:"\n[Recive  ] %s \n" % (self.packetStr_to_hex(pkt.original)))

            # for pkt in pkts:
                # print(self.packetStr_to_hex(pkt.original))



def sendMethod(target):
    while True:
        # time.sleep(1)
        packet2 = TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="Job", Parameters=S7SetConParameter(MaxAmQcalling=0x000A, MaxAmQcalled=0x000A))
        
        item = [("DB1", "2.0", "byte", 3)]
        transport_size, block_num, area_type, address = target.get_item_pram_from_item(item[0])
        length = int(item[0][3])
        READ_PACKET = TPKT() / COTPDT( EOT=1 ) /  S7Header(ROSCTR="Job", 
                                                               Parameters=S7ReadVarParameterReq(Items=S7ReadVarItemsReq(TransportSize=transport_size,
                                                                                                                        GetLength=length,
                                                                                                                        BlockNum=block_num,
                                                                                                                        AREAType=area_type,
                                                                                                                        Address=address
                                                                                                                        )))
        
        target.send_s7_packet(READ_PACKET)


if __name__ == '__main__':
    target = MyS7Client(name="test", ip="192.168.1.188", rack=0, slot=1)

    # target2 = MyS7Client(name="test", ip="192.168.178.11", rack=0, slot=2)

    target.connect()
    # target2.connect()

    sendThread = threading.Thread(target=sendMethod, args=(target,))
    # send2Thread = threading.Thread(target=sendMethod, args=(target2,))
    recvThread = threading.Thread(target=target.receive)
    recvThread.start()

    sendThread.start()
    # send2Thread.start()
    

    # recvThread.setDaemon(True)
    # a = input("continue")
    
    # sendThread.setDaemon(True)

