from scapy.all import *
from MIPlugin import MIPlugin
from BaseClass import Base  

from MyS7Client import MyS7Client
from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *

from BLocate import BLocate

class PluginException(Exception):
    pass

class PLCException(Exception):
    pass

class HandleCrush(Base):

    '''
        @parameter plugin: the MIPlugin object
        @parameter maxPluginCount: try to switch on/off max times
        @parameter maxWait: the max time to wait the PLC restart 
        @parameter maxWaitCount: the max wait times to wait PLC restart
    '''
    def __init__(self, s7Client, plugin, maxPluginCount=3, maxWait=3, maxWaitCount=3):
        super(HandleCrush, self).__init__()
        self.__plugin = plugin
        self.__maxPluginCount = maxPluginCount
        self.__maxWait = maxWait
        self.__maxWaitCount = maxWaitCount
        self.__S7Client = s7Client


    def getS7Client(self):
        return self.__S7Client

    '''
        @function: handle the crush 
            1.switch on the plugin
            2.switch off the plugin
            3.wait the plc to restart
            4.check whether the plc is online
        @raise PLCException: the plc is not online
    '''
    def handleCrush(self):

        self.__closePlugin()

        self.__openPlugin()

        i = self.__maxWaitCount

        while(i > 0):
            i = i - 1
            time.sleep(self.__maxWait)
            plcStatus = self.__S7Client.onlinePLC()
            if(plcStatus == True):
                return True
        
        raise PLCException("PLC restart failed!")
        


    '''
        @function: try to close the plugin 
        @raise PluginException: if switch off the plugin failed
    '''
    def __closePlugin(self):
        i = self.__maxPluginCount
        while(i > 0):
            i = i - 1
            res = self.__plugin.off()
            if(res == True):
                return True
        if(i == 0):
            raise PluginException("Switch off Plugin failed, Max_Count: " + self.__maxPluginCount)

    
    '''
        @function: try to open the plugin 
        @raise PluginException: if switch on the plugin failed
    '''
    def __openPlugin(self):
        i = self.__maxPluginCount
        while(i > 0):
            i = i - 1
            res = self.__plugin.on()
            if(res == True):
                return True

        if(i == 0):
            raise PluginException("Switch on Plugin failed, Max_Count: " + self.__maxPluginCount)




target = MyS7Client(name="test", ip="192.168.20.128", src_ip="192.168.20.1", rack=0, slot=1)

pkt = TPKT() / COTPDT( EOT=1 ) / S7Header(ROSCTR="UserData",
                                        Parameters=S7ReadSZLParameterReq(),
                                        Data=S7ReadSZLDataReq(SZLId=RandShort(),
                                                            SZLIndex=RandShort()))


item = [("DB1", "2.0", "byte", 3)]
transport_size, block_num, area_type, address = target.get_item_pram_from_item(item[0])
length = int(item[0][3])
crushPacket = TPKT() / COTPDT( EOT=1 ) /  S7Header(ROSCTR="Job", 
                                                Parameters=S7ReadVarParameterReq(Items=S7ReadVarItemsReq(TransportSize=transport_size,
                                                                                                        GetLength=length,
                                                                                                        BlockNum=block_num,
                                                                                                        AREAType=area_type,
                                                                                                        Address=address
                                                                                                        )))


target.connect()

a = input("continue")

packets = [pkt for i in range(100) ]
packets[20] = crushPacket

ip = "192.168.137.112"
token = "cf337484e9615f509fa39591bc802784"
plug = MIPlugin(ip=ip, token=token)
hc = HandleCrush(target, plug)
bl = BLocate(packets, hc)

ans = bl.locate()

