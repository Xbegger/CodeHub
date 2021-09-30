# coding:utf-8
import sys

# sys.path.append(".")

from MyS7Client import MyS7Client

def bLocateCrush(packets):
    
    # dict to list
    pktlist = list(packet.keys())
    # choose half of packets
    chosenPkt = pktlist / 2


    # send chosen packets

    # detect crush

    # choose half of packets
    return


target = MyS7Client(3, 3, "test", ip="192.168.20.128", rack=0, slot=3)

target.connect()


read_items = [("DB1", "0.0", "byte", 1)]

packet = target.getReadVarPacket(read_items)

target.send_s7_packet(packet)
target.send_s7_packet(packet)
target.send_s7_packet(packet)
target.send_s7_packet(packet)
rsp = target.receive_s7_packet()
target.close()