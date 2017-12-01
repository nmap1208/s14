#Auther nmap
import socket
import hashlib
client = socket.socket()
client.connect(("localhost",9998))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send( msg.encode("utf-8") )
    cmd_res_size = client.recv(1024) ##接受文件大小的长度
    print('需要接收的文件大小为:',int(cmd_res_size.decode()))
    client.send('ready to recive'.encode('utf-8'))
    f2=open('demo2.mp4','wb')
    received_size=0
    #received_data=b''
    m=hashlib.md5()
    while received_size<int(cmd_res_size.decode()) :
        data=client.recv(1024)
        m.update(data)
        f2.write(data)
        received_size += len(data) #每次收到的有可能小于1024，所以必须用len判断
        #received_data += data
    else:
        f2.flush()
        f2.close()
        print("cmd res receive done...",received_size)
        client.send('clinet received done'.encode())
        client_file_md5=m.hexdigest()
        server_file_md5=client.recv(1024).decode()
        if client_file_md5==server_file_md5:
            print('文件接收数据一致')
        else:
            print('文件不一致，请检查')
        #print(received_data.decode())
client.close()