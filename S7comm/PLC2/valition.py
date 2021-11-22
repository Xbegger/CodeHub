from random import Random
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
    def __init__(self, s7Client, plugin, maxPluginCount=3, maxWait=4, maxWaitCount=4):
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
        self.logger.info("handling crush")
        
        self.__closePlugin()

        time.sleep(2)

        self.__openPlugin()
        # self.logger.info("Switch on Plugin success!")

        plcStatus = self.__S7Client.onlinePLC(timeout=self.__maxWait, retry=self.__maxWaitCount)
        if(plcStatus == True):
            # self.logger.info("The PLC is online!")
            return True

        raise PLCException("PLC restart failed!")
        


    '''
        @function: try to close the plugin 
        @raise PluginException: if switch off the plugin failed
    '''
    def __closePlugin(self):
        self.logger.info("trying to switch off the plugin")
        i = self.__maxPluginCount
        while(i > 0):
            i = i - 1
            res = self.__plugin.off()
            if(res == True):
                self.logger.info("Switch off Plugin success!")
                return True
        if(i == 0):
            raise PluginException("Switch off Plugin failed, Max_Count: " + self.__maxPluginCount)
        
        

    
    '''
        @function: try to open the plugin 
        @raise PluginException: if switch on the plugin failed
    '''
    def __openPlugin(self):
        self.logger.info("trying to switch on the plugin")
        i = self.__maxPluginCount
        while(i > 0):
            i = i - 1
            res = self.__plugin.on()
            if(res == True):
                self.logger.info("Switch on the Plugin success!")
                return True

        if(i == 0):
            raise PluginException("Switch on Plugin failed, Max_Count: " + self.__maxPluginCount)
        



target = MyS7Client(name="test", ip="192.168.1.188", src_ip="192.168.1.137", rack=0, slot=1)

pkt = TPKT() / COTPDT( EOT=1 ) / S7Header(ROSCTR="UserData",
                                        Parameters=S7ReadSZLParameterReq(),
                                        Data=S7ReadSZLDataReq())


item = [("M", "0.1", "bit", 3)]
transport_size, block_num, area_type, address = target.get_item_pram_from_item(item[0])
length = int(item[0][3])
crushPacket = TPKT() / COTPDT( EOT=1 ) /  S7Header(ROSCTR="Job", 
                                                Parameters=S7ReadVarParameterReq(Items=S7ReadVarItemsReq(TransportSize=transport_size,
                                                                                                        GetLength=length,
                                                                                                        BlockNum=block_num,
                                                                                                        AREAType=area_type,
                                                                                                        Address=address
                                                                                                        )))



# target.connect()
# a = input("continue")




ip = "192.168.1.134"
token = "28aa291e4d034fe9a955d6e735153ae6"
plug = MIPlugin(ip=ip, token=token)
target.setCrushPacket(crushPacket, plug)
hc = HandleCrush(target, plug)
    
bl = BLocate(hc)

MAX_CANDIDATE = 40
MAX_PACKETS = 1000

crushListenThread = threading.Thread(target=target.crushListen)
crushListenThread.start()
while(True):
    # 生成模糊测试的报文
    packets = [pkt for i in range(MAX_PACKETS) ]
    crushNum = random.randint(0, 200)
    packets[crushNum] = crushPacket
    target.logger.info("Will send %d packets, the crush packet is %d" %(MAX_PACKETS, crushNum))

    candidatePackets = list()

    target.connect()
    # 开始监听PC端ARP
    target.run.set()

    # 发送模糊测试报文，检测到奔溃停止发送
    for pkt in packets: 
        target.send_s7_packet(pkt)
        time.sleep(0.2)

        # 处理候选集
        if(len(candidatePackets) == MAX_CANDIDATE):
            candidatePackets.pop(0)
            candidatePackets.append(pkt)
        else:
            candidatePackets.append(pkt)

        if(target.crush.is_set()):
            crush = not target.onlinePLC()
            if(crush == False):
                target.run.set()
            else:
                hc.handleCrush()
                ans = bl.locate(candidatePackets)
                findCrushNum = packets.index(ans)
                target.logger.info("The true crush number is %d, the finded crush number is %d" % (crushNum, findCrushNum))
                break


    
    # print(ans)

