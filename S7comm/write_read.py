from icssploit.clients.s7_client import S7Client

target = S7Client(name="test", ip="192.168.178.16", rack=0, slot=3)

target.connect()

write_items = [("DB1", "2.0", "byte", [10,20,30])]

read_items = [("DB1", "2.0", "byte", 3)]


recv = target.read_var(read_items)
print("Before Write:" ,recv)
target.write_var(write_items)
recv = target.read_var(read_items)
print("After write:", recv)
