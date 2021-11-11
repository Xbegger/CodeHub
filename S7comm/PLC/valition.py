from scapy.all import *
import MIPlugin
from baseClass import Base  


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
    def __init__(self, plugin, maxPluginCount, maxWait, maxWaitCount):
        super(HandleCrush, self).__init__()
        self.__plugin = plugin
        self.__maxPluginCount = maxPluginCount
        self.__maxWait = maxWait
        self.__maxWaitCount = maxWaitCount



    '''
        @function: handle the crush 
            1.switch on the plugin
            2.switch off the plugin
            3.wait the plc to restart
            4.chechk whether the plc is online
    '''
    def handleCrush(self):

        self.__closePlugin(self.__plugin, self.__maxPluginCount)

        self.__openPlugin(self.__plugin, self.__maxPluginCount)

        i = self.__maxWaitCount

        while(i > 0):
            i = i - 1
            time.sleep(self.__maxWait)
            plcStatus = onlinePLC()
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



'''
    @function: judge whethre the PLC is online by arp test
    @parameter string dstIP：the PLC IP
    @parameter string srcIP: the host IP
    @parameter int timeout: the max time to wait response
    @parameter int retry: the max try to send arp test
    @return bool true: PLC is online
    @return bool false: PLC is offline

'''
def onlinePLC(dstIP, srcIP, timeout, retry):
    packet = ARP(dst=dstIP, src=srcIP)

    recv = sr1(packet, retry=retry, timeout=timeout)
    if(recv != None):
        return True

    return False






