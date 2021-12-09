from icssploit.clients.s7_client import S7Client
from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *



class testClient(S7Client):

    def __init__(self, name, ip, port=102, src_tsap='\x01\x00', rack=0, slot=2, timeout=2):
        super(S7Client, self).__init__(name=name)
        self._ip = ip
        self._port = port
        self._slot = slot
        self._src_tsap = src_tsap
        self._dst_tsap = '\x01'.encode() + struct.pack('B', rack * 0x20 + slot)
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

    def write_var(self, items):
        """

        :param items:
        :return:
        """
        write_items = []
        items_data = []
        write_data_rsp = []
        if isinstance(items, list):
            for i in range(len(items)):
                try:
                    transport_size, block_num, area_type, address = self.get_item_pram_from_item(items[i])
                    length = len(items[i][3])
                    if transport_size:
                        write_items.append(S7WriteVarItemsReq(TransportSize=transport_size,
                                                              ItemCount=length,
                                                              BlockNum=block_num,
                                                              AREAType=area_type,
                                                              BitAddress=address
                                                              )
                                           )
                        write_data = self._pack_data_with_transport_size(write_items[i], items[i][3])
                        items_data.append(S7WriteVarDataItemsReq(
                            TransportSize=self._convert_transport_size_from_parm_to_data(transport_size),
                            Data=write_data))
                except Exception as err:
                    self.logger.error("Can't create write var packet because of: \r %s" % err)
                    return None
        else:
            self.logger.error("items is not list please check again")
            return None

        packet = TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="Job",
                                                   Parameters=S7WriteVarParameterReq(Items=write_items),
                                                   Data=S7WriteVarDataReq(Items=items_data))
        print(raw(packet))
        return
        rsp = self.send_receive_s7_packet(packet)
        if rsp.ErrorClass != 0x0:
            self.logger.error("Can't write var to Target.")
            self.logger.error("Error Class: %s, Error Code %s" % (rsp.ErrorClass, rsp.ErrorCode))
            return None
        if rsp.haslayer(S7WriteVarDataRsp):
            for rsp_items in rsp[S7WriteVarDataRsp].Items:
                write_data_rsp.append(rsp_items.ReturnCode)
            return write_data_rsp
        else:
            self.logger.error("Unknown response packet format.")
            return None


target = testClient(name="test", ip="192.168.1.1")
write_items = [("M", "20.0", "real", [0.1, 1.1])]

target.write_var(write_items)