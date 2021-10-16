# coding:utf-8
from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *
import socket
from scapy.compat import raw

HOST = '192.168.178.23'
PORT = 8888

ADDRESS = (HOST, PORT)

udpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packet2 = S7Header(ROSCTR="Job", Parameters=S7SetConParameter(MaxAmQcalling=0x000A, MaxAmQcalled=0x000A))



# 发送数据
udpClientSocket.sendto(raw(packet2), ADDRESS)