#Auther nmap

import socket

HOST = 'localhost'    # The remote host
PORT = 10000          # The same port as used by the server
s = socket.socket()
s.connect((HOST, PORT))
while True:
    msg = bytes(input(">>:"),encoding="utf8")
    s.sendall(msg)
    data = s.recv(1024)
    #print(data)

    print('Received', repr(data))
s.close()