import time
from MIPlugin import MIPlugin
from MyS7Client import MyS7Client
from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *
from scapy.all import *
from arpcapture import *
import random
import pymongo
import datetime

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.base
db.send_packet.drop()
db.crush_packet.drop()
db.conf.drop()
send_packet_db = db.send_packet
crush_packet_db = db.crush_packet
configuration = db.conf
now_time = datetime.datetime.now()
time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
fuzz_field = ['读数据ReadVar', '写数据WriteVar', '读取状态ReadSZL']
configuration.insert_one({'测试协议': 'Siemens S7',
                          '设备型号': 'PLC-1200',
                          '创建时间': time_str,
                          '创建人': 'dsy',
                          '模糊字段': fuzz_field[0]})

ip = "192.168.1.134"
token = "28aa291e4d034fe9a955d6e735153ae6"
plug = MIPlugin(ip=ip, token=token)


def replace_packet(packet_set, new_packet):
    for i in range(0, len(packet_set)-1):
      packet_set[i] = packet_set[i+1]
    packet_set[len(packet_set)-1] = new_packet

def send_packet(packet, num):
  now_time = datetime.datetime.now()
  time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
  packet_str = raw(packet).hex()
  send_packet_db.insert_one({'_id': num, 'time': time_str, 'packet': packet_str})
  target.send_receive_my_packet(packet)


def bi_send_packet(packet):
  target.send_my_packet(packet)


def find_packet(packet_set):
  print('start finding crush packet')
  target.connect()
  Len = len(packet_set)
  start = 0
  end = Len-1
  print(Len)
  while(end-start != 1): #end-start==1则表示已经定位到了
    print('range:', (start, int((start+end+1)/2)-1))
    for i in range(start, int((start+end+1)/2)):
      bi_send_packet(packet_set[i])
      time.sleep(0.2)
    time.sleep(5)
    is_crush = not target.onlinePLC()
    if is_crush == False:
      start = int((start+end+1)/2)
      Len = Len/2
    else:
      end = int((start+end+1)/2)
      Len = Len/2
      plug.on()  #因为发送了含有崩溃报文的那一部分，PLC已关闭，需要重启。
      time.sleep(10)
      target.connect()#每次重启后都需要重新连接
    print(start, end)
  crush_packet_str = raw(packet_set[start]).hex()
  crush_packet_db.insert_one({'packet': crush_packet_str})
  print('The crush packet is:', start, raw(packet_set[start]).hex())
  plug.on()
  time.sleep(10)
  target.connect()

target = MyS7Client(name="test", ip="192.168.1.188", src_ip="192.168.1.101", rack=0, slot=1)
# target.onlinePLC()
target.connect()
read_Packet = TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="Job",
                                                  Parameters=S7ReadVarParameterReq(Items=S7ReadVarItemsReq(TransportSize=RandEnumKeys(S7_TRANSPORT_SIZE_IN_PARM_ITEMS),
                                                                                                           GetLength=RandShort(),
                                                                                                           BlockNum=RandShort(),
                                                                                                           AREAType=RandEnumKeys(S7_AREA_TYPE),
                                                                                                           Address=RandShort()*RandByte()
                                                                                                          )))
READ_SZL_PACKET = TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="UserData",
                                                    Parameters=S7ReadSZLParameterReq(),
                                                    Data=S7ReadSZLDataReq(SZLId=RandShort(), SZLIndex=RandShort()))
error_packet = []
packet_set = [read_Packet for i in range(64)]

arp_capture_thread = ArpCaptureThread(capture_arp)
arp_capture_thread.start()
fuzz_count = 0
while(True):
  packet = read_Packet
  fuzz_count = fuzz_count+1
  if arp_capture_thread.get_result() == False:
    replace_packet(packet_set, packet)
    send_packet(packet, fuzz_count)
    time.sleep(0.2)
  else:
    if target.onlinePLC() == False:
      plug.on()
      time.sleep(10)
      find_packet(packet_set)
    else:
      arp_capture_thread.result = False
      error_packet.append(packet)
