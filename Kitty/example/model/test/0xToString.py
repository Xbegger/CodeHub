import binascii
from icssploit.protocols.cotp import *
from icssploit.protocols.s7comm import *
# while True:
#     string = input("请输入要转换的数字")
#     num = int(string, 16)

#     hexNum = hex(num)
#     # print(hexNum)

#     bStr = bytearray.fromhex(string)

#     ans = str(bStr)

#     print('对应的字符串为:' + ans)


# bNum = '0100'.encode('utf-8')
# print(bNum)

temp = b'A123'
temp = temp.decode()
print(temp)
# print(type(temp), temp) 
# temp = temp.hex()
# print(temp)



# s =  TPKT() / COTPDT( EOT=1 ) / S7Header(ROSCTR="UserData",
#                                         Parameters=S7ReadSZLParameterReq(),
#                                         Data=S7ReadSZLDataReq())

# print(raw(s).hex())
# print(type(str(s)))


a="\\xE8\\xA5\\xBF\\xE8\\x97\\x8F\\xE8\\x87\\xAA\\xE6\\xB2\\xBB\\xE5\\x8C\\xBA"

# 转成bytes
a=bytes(a, 'utf-8')

print(type(a))
print(a)
b=a.decode('unicode_escape').encode('latin1').decode('utf-8')

print(b)

a = "b'\\x33\\x01\\x02\\x03'"
a=bytes(a, 'utf-8')
print(a)
payload = a.decode('unicode_escape')[2:-1].encode()
print(type(payload))
print(payload)