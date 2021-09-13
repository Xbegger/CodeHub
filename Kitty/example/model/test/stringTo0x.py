
str = input("请输入要转换的字符串")
by = bytes(str, 'UTF-8')
print(by.hex())


'''
String: GET /index.html HTTP/1.1
16进制表示: 474554202f696e6465782e68746d6c20485454502f312e31

'''