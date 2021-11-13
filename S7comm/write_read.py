from icssploit.clients.s7_client import S7Client

target = S7Client(name="test", ip="192.168.1.188", rack=0, slot=1)

target.connect()

write_items = [("DB1", "1.0", "byte", [10])]
# write_items = [("M", "0.1", "bit", [1])]
read_items = [("DB1", "1.0", "byte", 1)]

# test write
# recv = target.read_var(read_items)
# print("Before Write:" ,recv)
target.write_var(write_items)
recv = target.read_var(read_items)
print("After write:", recv)


# light controller 
# target.write_var(write_items)