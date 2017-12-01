#Auther nmap
import socket
client=socket.socket()
client.connect(('127.0.0.1',9999))
while True:
    str=input('pls input your msg>>>:').strip()
    client.send(str.encode('utf-8'))
    client_recv=client.recv(1024)
    print('from server:',client_recv.decode())

client.close()