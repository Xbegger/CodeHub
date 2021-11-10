# coding:utf-8
from scapy.all import *

# print(show_interfaces())

lan = "Realtek PCIe GbE Family Controller"

# pkts = sniff(iface=lan, count=10, filter="arp")

# print(pkts)

p = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst='192.168.178.0/24')

ans, unans = srp(p, iface=lan, timeout=5)

print('The number of detected hosts are', len(ans))

result = []

for s, r in ans:
    result.append([r[ARP].psrc, r[ARP].hwsrc])


result.sort()

for ip, mac in result:
    print(ip, '-------------->', mac)
