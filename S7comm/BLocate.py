# coding:utf-8
import sys
import os
import threading
import time
import Queue
# sys.path.append(".")

from MyS7Client import MyS7Client

isCrush = threading.Event()
HeartBeatTime = 0.5

def bLocateCrush( orignalPackets):
    
    # dict to list
    pktList = orignalPackets
    # choose half of packets
    startPktList = 0
    pktListLength = len(pktList)
    endPktList = pktListLength
    
    # init stack
    stack = list()
    stack.append(endPktList)
    stack.append(startPktList)
    chosenPktLength = endPktList - startPktList

    while len(stack) > 0 and (chosenPktLength >= 1):
        # choose packets
        startPktList = stack.pop()
        endPktList = stack.pop()

        chosenPktLength = (endPktList - startPktList) / 2
        chosenPkt = pktList[startPktList : startPktList + chosenPktLength]

        # append have not be chosen packets
        stack.append(endPktList)
        stack.append(startPktList + chosenPktLength)
        # send chosen packets
        flag, tempPkt = sendTestPackets(client, chosenPkt)

        # detect crush
        if flag == False:
            # first half has crush
            stack.append(startPktList + chosenPktLength)
            stack.append(startPktList)
            # if find the crush packet
            if chosenPktLength == 1:
                break

    
    return chosenPkt

def sendTestPackets(client, packets):
    for pkt in packets:
        if isCrush.is_set():
            client.send_s7_packet(pkt)
        else:
            return False, packets
    
    if len(client.notResponsePackets) == 0:
        return True, None
    else:
        return False, packets


def heartBeatDetect(ip):

    isCrush.set()

    while True:
        pingResult = os.system('ping %s' % ip)

        if pingResult == 0:
            print("----Access %s successfully----" % ip)
            isCrush.set()
        else:
            print("----Access %s is timeout" % ip)
            isCrush.clear()
        time.sleep(HeartBeatTime)
        
        


PLC_IP = "192.168.20.128"

# target = MyS7Client(callingMaxAmQ=3, calledMaxAmQ=3, "test", ip=PLC_IP, rack=0, slot=3)

# target.connect()

# start Daemon Thread heart beat detect
heartBeatDetectThread = threading.Thread(target=heartBeatDetect, args=(PLC_IP,))
heartBeatDetectThread.setDaemon(True)
heartBeatDetectThread.start()

packets = []
bLocateCrush(packets)


# read_items = [("DB1", "0.0", "byte", 1)]

# packet = target.getReadVarPacket(read_items)

# target.send_s7_packet(packet)
# target.send_s7_packet(packet)
# target.send_s7_packet(packet)
# target.send_s7_packet(packet)
# rsp = target.receive_s7_packet()
# target.close()