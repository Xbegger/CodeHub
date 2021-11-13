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

# temp = b'0123'
# print(type(temp), temp) 
# temp = temp.hex()
# print(temp)



s =  TPKT() / COTPDT( EOT=1 ) / S7Header(ROSCTR="UserData",
                                        Parameters=S7ReadSZLParameterReq(),
                                        Data=S7ReadSZLDataReq())

print(raw(s).hex())
print(s)

