#Auther nmap
import socket
client2 = socket.socket()  #生成一个socket实例，socket模块的socket类
client2.connect(('localhost',6969))

while True:
    msg=input('>>>:').strip()
    client2.send(msg.encode('utf-8'))
    data=client2.recv(1024)
    print('recv:',data.decode())

client2.close()