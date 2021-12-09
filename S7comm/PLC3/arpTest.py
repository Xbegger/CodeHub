
from scapy.all import *


src_ip = "192.168.1.137"
dst_ip = "192.168.1.188"
time.sleep(2)
packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=dst_ip, psrc=src_ip)

recv = srp1(packet, retry=10, timeout=3)