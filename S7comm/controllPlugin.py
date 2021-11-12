#-*-coding:utf8-*-

import codecs

import socket
from time import sleep

from miio.protocol import Message
import datetime

ip = '192.168.137.35'

helobytes=bytes.fromhex('21310020ffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
openBytes = bytes.fromhex("21310090000000001c5540b8000005980bf70eba44316b34456472e32905b93bf3595ccb08ed6fb9b9f4464b8f5c22263c9867a7dbb8d6f77d0c12722699f3bfaf1ea51111ca2113b15a9f24d2d6230a83b719eb485dd2c6d5e0ee612f286a479a5393a6d199a49983b7e07f2b61234acfdafcea65e0c705b9c19c638a32b38b5b25d6264fda8c77bc53403a13c31db6")

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto(helobytes,(ip, 54321))#插座ip，端口54321
s.sendto(helobytes,(ip, 54321))#插座ip，端口54321
s.sendto(helobytes,(ip, 54321))#插座ip，端口54321
sleep(1)
s.sendto(openBytes,(ip, 54321))#插座ip，端口54321

# data,addr=s.recvfrom(1024)

# m=Message.parse(data)

# tok=codecs.encode(m.checksum,'hex')

# # print(m)

# # print(tok)

# ts=m.header.value.ts + datetime.timedelta(seconds=1)

# cmd={'id':1,'method':'set_power','params':['on']}

# header={'length':0,'unknown':0x00000000,                  

#           'device_id':bytes.fromhex('1c5540b8'),'ts':ts}

# msg={'data':{'value':cmd},

#        'header':{'value':header},

#        'checksum':0}

# tok = bytes.fromhex("908c4fe7d7121a963c642d485be4beaf")
# m0=Message.build(msg,token=tok)

# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# print(Message.parse(m0,token=tok))

# s.sendto(m0,(ip, 54321))

# data,addr=s.recvfrom(1024)
# data = "21310090000000001c5540b8000005980bf70eba44316b34456472e32905b93bf3595ccb08ed6fb9b9f4464b8f5c22263c9867a7dbb8d6f77d0c12722699f3bfaf1ea51111ca2113b15a9f24d2d6230a83b719eb485dd2c6d5e0ee612f286a479a5393a6d199a49983b7e07f2b61234acfdafcea65e0c705b9c19c638a32b38b5b25d6264fda8c77bc53403a13c31db6"
# m1=Message.parse(bytes.fromhex(data),token=tok)

# print(m1)