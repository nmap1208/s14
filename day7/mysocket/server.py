#Auther nmap
import socket
server=socket.socket()
server.bind(('0.0.0.0',9999))
server.listen()
print('劳资已经准备好了:')
# print(server.accept())
conn,addr=server.accept()
print(conn,addr)
print('对方进门了:')
while True:
    data=conn.recv(1024)
    print(data)
    print('from client:',data.decode())
    server_str=data.decode().upper()
    conn.send(server_str.encode('utf-8'))

server.close()