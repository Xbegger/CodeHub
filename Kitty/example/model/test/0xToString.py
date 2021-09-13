import binascii

while True:
    string = input("请输入要转换的数字")
    num = int(string, 16)

    hexNum = hex(num)
    # print(hexNum)

    bStr = bytearray.fromhex(string)

    ans = str(bStr)

    print('对应的字符串为:' + ans)


