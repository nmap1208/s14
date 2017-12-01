#Auther nmap
import socket
import os
import hashlib

server = socket.socket() #获得socket实例
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("localhost",9998)) #绑定ip port
server.listen()  #开始监听

while True: #第一层loop
    print("等待客户端的连接...")
    conn,addr = server.accept() #接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
    print("新连接:",addr )
    while True:

        data = conn.recv(1024)
        if not data:
            print("客户端断开了...")
            break #这里断开就会再次回到第一次外层的loop
        print("收到命令:",data.decode())
        cmd,file=data.decode().split()
        #res = os.popen(data.decode()).read() #py3 里socket发送的只有bytes,os.popen又只能接受str,所以要decode一下
        if os.path.isfile(file):
            print('需要的文件存在...')
            file_size=os.stat(file).st_size
            conn.send(str(file_size).encode())
            print('已经发送文件大小....')
            conn.recv(1024)#客户端表示已经准备接收了
            print('客户端已经做好接收准备')
            f=open(file,'rb')
            m=hashlib.md5()
            for line in f:
                m.update(line)
                conn.send(line)
            f.close()
            print('send file data done...')
            conn.recv(1024)  #客户端表示接收完毕了
            file_md5=m.hexdigest()
            conn.send(file_md5.encode())
            print('send md5 done...')


server.close()