#Auther nmap
import socket

client = socket.socket()

client.connect(("localhost",9998))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send( msg.encode("utf-8") )

    # data = client.recv(1024)
    # print(type(data))
    # print(data.decode())
    #print(client.recv(1024))
    len_res_b=int(client.recv(1024).decode())
    # print()
    client.send('ready to recive'.encode('utf-8'))
    recv_len=0
    recv_data=''
    print(type(recv_str))
    while recv_len<len_res_b:
        str_b=client.recv(1024)
        print(type(str_b))
        str_len=len(str_b)
        print(str_len)
        print(type(str_b.decode()))
        recv_str=recv_str+str_b.decode('utf-8')
        recv_len+=str_len
    print(recv_str)
client.close()
