#Auther nmap
import socket

client = socket.socket()
client.connect(("localhost",9998))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send( msg.encode("utf-8") )
    cmd_res_size = client.recv(1024) ##接受命令结果的长度
    client.send('ready to recive'.encode('utf-8'))
    received_size=0
    received_data=b''
    while received_size<int(cmd_res_size.decode()) :
        data=client.recv(1024)
        received_size += len(data) #每次收到的有可能小于1024，所以必须用len判断
        received_data += data
    else:
        print("cmd res receive done...",received_size)
        print(received_data.decode())
client.close()