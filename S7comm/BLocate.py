import sys

# sys.path.append(".")

from MyS7Client import MyS7Client



target = MyS7Client(0x0003, 0x0003, "test", ip="192.168.178.21", rack=0, slot=3)

target.connect()