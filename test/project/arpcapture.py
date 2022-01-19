from scapy.all import *
import threading

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
        return ip

def Get(a):
    print("capture target ARP packet")


def stopFilter1(x):
    if x.pdst == "192.168.1.188":
        return True
    else:
        return False

def capture_arp():
    packet = sniff(filter="arp and dst host 192.168.1.188 and src host " + get_host_ip(),
                prn=Get,
                stop_filter=stopFilter1)
    
    # print("arp capture")
    # if packet[0].pdst == '192.168.1.188':
    #     plugin.on()
    #     return True

class ArpCaptureThread(threading.Thread):
    def __init__(self,func):
        super(ArpCaptureThread,self).__init__()
        self.func = func
        # arp 获取的返回值
        self.result = False
        self.__flag = threading.Event()     # 用于暂停线程的标识
        self.__flag.set()       # 设置为True
        self.__running = threading.Event()      # 用于停止线程的标识
        self.__running.set()      # 将running设置为True

    def run(self):
        while self.__running.isSet():
            self.__flag.wait()
            self.result = self.func()
    
    def get_result(self):
        try:
            return self.result
        except Exception:
            return False

    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()        # 设置为False    

