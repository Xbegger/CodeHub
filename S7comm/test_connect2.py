# coding:utf-8
from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *
import socket
from scapy.compat import raw


packet2 = TPKT() / COTPDT(EOT=1) / S7Header(ROSCTR="Job", Parameters=S7SetConParameter(MaxAmQcalling=0x000A, MaxAmQcalled=0x000A))

ip = "192.168.1.13"
server_address = (ip, 102)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# input("continue")

s.sendto(raw(packet2), server_address)
