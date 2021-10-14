# coding:utf-8
import os

ip = '192.168.1.188'
port = 111
while True:
    pingResult = os.system('tcping 192.168.1.188 %s' % port)

    if pingResult != 0:
        port = port + 1
    else:
        break

# 25 110
