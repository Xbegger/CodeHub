from verifyClient import Client
from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *
from MIPlugin import MIPlugin
import threading
import random


def activeDetect():
    return target.activeDetect(timeout=3, retry=3)

def passiveDetect():
    target.passiveDetect(passiveCallback)

def passiveCallback(pkts):
    target.logger.info("passiveDetect find a Crush")
    for pkt in pkts:
        print(str(pkt))
    crush.clear()
 

mutex = threading.Lock()
recvCount = 0
def recvPkt():
    global recvCount
    if(recvCount > 0):
        target.receive_s7_packet()
        mutex.acquire()
        recvCount = recvCount - 1
        mutex.release()



target = Client(name="test", ip="192.168.1.188", src_ip="192.168.1.141", rack=0, slot=1)

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


ip = "192.168.1.134"
token = "28aa291e4d034fe9a955d6e735153ae6"
plug = MIPlugin(ip=ip, token=token)
target.setCrushPacket(crushPacket, plug)


# 被动监听的线程
crush = threading.Event()
crush.set()
crushListenThread = threading.Thread(target=passiveDetect)
crushListenThread.start()


# 接受报文的线程
recvThread = threading.Thread(target=recvPkt)
recvThread.start()

count = 0
# 发送报文
## 发送 100 个报文，中间有1 个奔溃报文
testTimes = 100

logger = target.logger
target.connect()
for i in range(0, testTimes):

    crushPkt = random.randint(1, 100)
    
    logger.info("The Crush Packet is %d" % (crushPkt))

    j = 0
    while(True):
        if( j != crushPkt):
            target.send_s7_packet(pkt)
        else:
            target.send_s7_packet(crushPacket)

        time.sleep(0.1)
        mutex.acquire()
        recvCount = recvCount + 1
        mutex.release()

        j = j + 1
        if(not crush.is_set()):
            # 被动监听到奔溃
            ## 主动监听验证被动监听的正确性
            ans = activeDetect()
            
            logger.info("No: %d, sended packets %d ,passiveDetected find a Crush, The activeDetect ans is %s" \
                                %(i, j, "Online" if ans else "Crush"))

            # 奔溃处理
            if not ans:
                count = count + 1
                plug.on()
                time.sleep(8)
                target.close()
                target.connect()
                time.sleep(4)

            # 被动监听的线程
            crush = threading.Event()
            crush.set()
            crushListenThread = threading.Thread(target=passiveDetect)
            crushListenThread.start()
            break


target.logger.info("The accurate is %f, the true case is %d" %(count / testTimes, count))


