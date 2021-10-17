# coding:utf-8
from icssploit.clients.base import Base
from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *
from scapy.supersocket import StreamSocket
import socket
from icssploit.clients.s7_client import S7Client
from scapy.compat import raw

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
        super(MyS7Client, self).__init__(name, ip, port=102, src_tsap='\x01\x00', rack=0, slot=2, timeout=2)
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
        packet2 = TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="Job", Parameters=S7SetConParameter(MaxAmQcalling=0x000A, MaxAmQcalled=0x000A))
        rsp2 = self.send_receive_s7_packet(packet2)
        if rsp2:
            self._connected = True
        # Todo: Need get pdu length from rsp2

    def send_s7_packet(self, packet):
        if self._connection:
            packet = self._fix_pdur(packet)
            try:
                self._connection.send(packet)
                self.pktCounts = self.pktCounts + 1
                msg = "[Time:" + time.strftime("%H:%M:%S" , time.localtime()) + "]    [Packet Number:" + str(self.pktCounts) + "]\n"
                msg = msg + "        [Content: " + self.packetStr_to_hex(raw(packet)) + "]\n"
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


target = MyS7Client(name="test", ip="192.168.178.21", rack=0, slot=3)

target.connect()

# a = input("continue")
packet2 = TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="Job", Parameters=S7SetConParameter(MaxAmQcalling=0x000A, MaxAmQcalled=0x000A))
target.send_s7_packet(packet2)