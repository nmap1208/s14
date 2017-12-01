#Auther nmap
import socket
server=socket.socket()
server.bind(('localhost',6969)) #绑定要监听端口

server.listen() #监听
print('我要等电话了')
while True:
    conn,addr=server.accept()#等电话打进来
    print(conn,addr)
    print('电话来了')
    while True:
        data=conn.recv(1024)
        print('recv:',data)
        if not data:
            break
        conn.send(data.upper())

    server.close()