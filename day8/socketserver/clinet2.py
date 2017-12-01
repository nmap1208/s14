#Auther nmap
#Auther nmap
import socket
client=socket.socket()
client.connect(('localhost',9999))
while True:
    data=input('>>>:')
    if len(data) >0:
        client.send(data.encode('utf-8'))
        data_recv=client.recv(1024)
        print(data_recv)