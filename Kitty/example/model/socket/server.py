import socket

mysocket = socket.socket()

host = socket.gethostname()
port = 26010
mysocket.bind((host, port))

mysocket.listen(5)

while True:
    c, addr = mysocket.accept()
    print('连接地址：', addr)
    c.send(str.encode('欢迎访问！'))
    c.close()