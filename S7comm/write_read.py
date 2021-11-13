from icssploit.clients.s7_client import S7Client

target = S7Client(name="test", ip="192.168.1.188", rack=0, slot=1)

target.connect()

input("abc")
# DB_items = [("DB1", "2.0", "byte", [10,20,30])]
M_write = [("M", "0.0", "bit", [1])]
M_read = [("M", "0.0", "bit", 1)]

# DB_items = [("DB1", "2.0", "byte", 3)]

read_items = M_read
write_items = M_write

recv = target.read_var(read_items)

print("Before Write:" ,recv)
target.write_var(write_items)
recv = target.read_var(read_items)
print("After write:", recv)
