import socket

mysocket = socket.socket()

host = socket.gethostname()
port = 12345

mysocket.connect((host, port))

print( bytes.decode(mysocket.recv(1024)))

mysocket.close()