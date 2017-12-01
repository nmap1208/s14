#Auther nmap
import socket
server=socket.socket()
server.bind(('localhost',9999))
server.listen(5)

while True:
    conn,addr=server.accept()
    data=conn.recv(1024)
    print('recv:>>>',data)
    conn.send(data)