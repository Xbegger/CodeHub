from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *
from scapy.supersocket import StreamSocket
import socket
from BaseClass import Base
from scapy.all import *

VAR_NAME_TYPES = {
    'P': 0x80,      # I/O
    'I': 0x81,      # Memory area of inputs
    'Q': 0x82,      # Memory area of outputs
    'M': 0x83,      # Memory area of bit memory
    'DB': 0x84,     # Data block
    'L': 0x86,      # Local data
    'V': 0x87       # Previous local data
}


class MyS7Client(Base):
    
    def __init__(self, name, ip, src_ip, port=102, src_tsap='\x01\x00', rack=0, slot=2, timeout=2):
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
        self.crushPacket = None
        self._plugin = None
        self._src_ip = src_ip


    def connect(self):
        sock = socket.socket()
        # sock.settimeout(self._timeout)
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
                msg = "[Connect request]" + raw(packet).hex()
                self.logger.info(msg)
                if rsp:
                    rsp = TPKT(raw(rsp))
                    msg = "[Connect responde]" + raw(rsp).hex()
                    self.logger.info(msg)
                return rsp

            except Exception as err:
                self.logger.error(err)
                return None

        else:
            self.logger.error("Please create connect before send packet!")


    def send_s7_packet(self, packet):
        if self._connection:
            initPacket = packet
            packet = self._fix_pdur(packet)
            try:
                self._connection.send(packet)
                if(self.crushPacket != None and initPacket == self.crushPacket):
                    self._plugin.off()
                    self.logger.info("Send the crush packet")
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
    
    def get_item_pram_from_item(self, item):
        block_num = ''
        area_type = ''
        address = ''
        transport_size = ''
        try:
            for key in VAR_NAME_TYPES:
                if isinstance(item[0], str):
                    if item[0].startswith(key):
                        area_type = VAR_NAME_TYPES[key]

                elif isinstance(item[0], int):
                    if item[0] in VAR_NAME_TYPES.keys():
                        area_type = item[0]

            # Data block
            if area_type == 0x84:
                block_num = int(item[0][2:])
            else:
                block_num = 0

            if isinstance(item[1], str):
                address_data = item[1].split('.')
                address = int(address_data[0]) * 8 + int(address_data[1])

            elif isinstance(item[1], int):
                address = item[1]

            else:
                self.logger.error("Address: %s is not string or int format, please check again" % item[1])

            transport_size = self.get_transport_size_from_data_type(item[2])

        except Exception as err:
            self.logger.error("Can't get item parameter with var_name: %s with error: \r %s" % (item, err))
            return transport_size, block_num, area_type, address

        return transport_size, block_num, area_type, address

    @staticmethod
    def get_transport_size_from_data_type(data_type):
        for key, name in S7_TRANSPORT_SIZE_IN_PARM_ITEMS.items():
            if isinstance(data_type, str):
                if name.startswith(data_type.upper()):
                    return key
            elif isinstance(data_type, int):
                return data_type
        return None



    def setCrushPacket(self, crushPacket, plugin):
        self.crushPacket = crushPacket
        self._plugin = plugin


    '''
        @function: judge whether the PLC is online by arp test
        @parameter string dstIP：the PLC IP
        @parameter string srcIP: the host IP
        @parameter int timeout: the max time to wait response
        @parameter int retry: the max try to send arp test
        @return bool true: PLC is online
        @return bool false: PLC is offline

    '''
    def onlinePLC(self, timeout = 3, retry=1):
        self.logger.info("checking whether the PLC is online")
        packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=self._ip, psrc=self._src_ip)

        recv = srp1(packet, retry=retry, timeout=timeout)
        if(recv != None):
            self.logger.info("the PLC is online")
            return True

        self.logger.info("the PLC is offline")
        return False





