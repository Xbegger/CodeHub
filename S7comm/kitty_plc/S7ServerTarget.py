from binascii import hexlify
from struct import pack
import traceback
from kitty.core import KittyException
from kitty.targets.base import BaseTarget
from kitty.data.report import Report
from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *
from scapy.supersocket import StreamSocket


class S7ServerTarget(BaseTarget):
    def __init__(self, name, ip, port=102, src_tsap='\x01\x00', rack=0, slot=2,\
                max_retries=10, timeout=2, logger=None):
        super(S7ServerTarget, self).__init__(name, logger)
        self._ip = ip
        self._port = port
        self._src_tsap = src_tsap
        self._dst_tsap = "\x01".encode() + struct.pack('B', rack * 0x20 + slot)
        self._connection = None
        self._connected = False
        self.max_retries = max_retries
        self.timeout = timeout
        self._pdu_length = 480
        self._pdur = 1
        self.send_failure = False
        self.transmission_count = 0
        self.transmission_report = None
    
    @classmethod
    def COTP_CR_Packet(cls, src_tsap, dst_tsap):
        packet = TPKT() / COTPCR()
        packet.Parameters = [COTPOption() for i in range(3)]
        packet.PDUType = "CR"
        packet.Parameters[0].ParameterCode = "tpdu-size"
        packet.Parameters[0].Parameter = "\x0a"
        packet.Parameters[1].ParameterCode = "src-tsap"
        packet.Parameters[2].ParameterCode = "dst-tsap"
        packet.Parameters[1].Parameter = src_tsap
        packet.Parameters[2].Parameter = dst_tsap
        return packet

    @classmethod
    def S7_CR_Packet(cls, MaxAmQcalling=0x000A, MaxAmQcalled=0x000A, PDULength=0x01E0):
                packet = TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="Job", 
                                                    Parameters=S7SetConParameter(MaxAmQcalling=MaxAmQcalling, 
                                                                                 MaxAmQcalled=MaxAmQcalled,
                                                                                 PDULength=PDULength))
   
    def connect(self):
        '''
        Connected to the plc,if the target hasn't connected to the plc
        
        '''
        if self._connected is not None:

            retry_count = 0
            while self._connection is None and retry_count < self.max_retries:
                sock = socket.socket()
                if self.timeout is not None:
                    sock.settimeout(self.timeout)
                try:
                    retry_count += 1
                    sock.connect((self._ip, self._port))
                    self._connection = StreamSocket(sock, Raw)
                    self.S7ServerConnect()
                except Exception:
                    sock.close()
                    self.logger.error('Error: %s' % traceback.format_exc())
                    self.logger.error('Failed to connect to target server, retrying...')
                    time.sleep(1)
            
            if self._connection is None:
                raise(KittyException('S7ServerTarget:(connect) cannot connect to server (retries = %d' % retry_count))


    
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

    def S7ServerConnect(self):
        packet = self.COTP_CR_Packet(self._src_tsap, self._dst_tsap)
        self.send_receive_s7_packet(packet)
        packet = self.S7_CR_Packet(PDULength=self._pdu_length)
        self.send_receive_s7_packet(packet)

    def send_s7_packet(self, packet):
        if self._connection:
            initPacket = packet
            packet = self._fix_pdur(packet)
            try:
                self._connection.send(packet)
                if(self.crushPacket != None and initPacket == self.crushPacket):
                    self._plugin.off()
                    self.logger.info("Send the crush packet")
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


    def pre_test(self, test_num):
        super(S7ServerTarget, self).__init__(test_num)
        self.send_failure = False
        self.transmission_count = 0

    def transmit(self, payload):
        '''
        Transmit single S7 packet payload

        :type payload:str
        :param payload: payload to send
        '''
        trans_report_name = 'transmission_0x%04x' % self.transmission_count
        trans_report = Report(trans_report_name)
        self.transmission_report = trans_report
        self.report.add(trans_report_name, trans_report)

        try:
            trans_report.add('request (hex)', hexlify(payload).decode)
            trans_report.add('request (raw)', '%s' % payload)
            trans_report.add('request length', len(payload))
            trans_report.add('request time', time.time())

            request = hexlify(payload).decode()
            request = request if len(request) < 100 else (request[:100] + '...')
            self.logger.info('request(%d):%s' % (len(payload), request))
            self.send_s7_packet(payload)
        except Exception as ex1:
            trans_report.failed('failed to send payload: %s' % ex1)
            trans_report.add('traceback', traceback.format_exc())
            self.logger.error('target.transmit - failuer in send (exception: %s)' % ex1)
            self.logger.error(traceback.format_exc())
            self.send_failure = True
        self.transmission_count += 1
        

    def post_test(self, test_num):
        super(S7ServerTarget, self).post_test(test_num)
        if self.send_failure:
            self.report.failed('send failure')
        
        
    


