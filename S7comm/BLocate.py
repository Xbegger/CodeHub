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
    
    
    stack.append(startPktList + pktListLength + 1)
    stack.append(startPktList)
    while len(stack) > 0:
        # choose packets
        startPktList = stack.pop()

        if len(stack > 0):
            endPktList = stack.pop() - 1
            stack.append(endPktList + 1)
        else:
            endPktList = pktListLength

        chosenPkt = pktList[startPktList: endPktList]
        chosenPktLength = endPktList - startPktList
        # send chosen packets
        #flag, tempPkt = sendTestPackets(client, chosenPkt)
        flag = True
        # detect crush
        if flag == True:
            # first half has not crush
            startPktList = startPktList + chosenPktLength
        # next test packets length
        pktListLength = pktListLength / 2
        # choose half of packets
        chosenPkt = pktList[startPktList: startPktList+pktListLength]
    
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

bLocateCrush(range(20))

# read_items = [("DB1", "0.0", "byte", 1)]

# packet = target.getReadVarPacket(read_items)

# target.send_s7_packet(packet)
# target.send_s7_packet(packet)
# target.send_s7_packet(packet)
# target.send_s7_packet(packet)
# rsp = target.receive_s7_packet()
# target.close()