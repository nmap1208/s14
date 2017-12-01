#Auther nmap
import select
import socket
import sys
import queue

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
server.bind(server_address)
server.listen(100)
server.setblocking(0)  #0表示False，表示是非阻塞模式,之前server.accept（）是阻塞的

msg_dic={}  #引入字典，存不同链接的数据
# Bind the socket to the port
print ('>>',sys.stderr, 'starting up on %s port %s' % server_address)

inputs = [ server ]
outputs = [ ]
while True:
    readble,writeable,exceptional=select.select(inputs,outputs,inputs)
    print(readble,writeable,exceptional)
    for r in readble:
        if r is server:  #如果活动的是server，表示来了个新链接
            conn,addr=server.accept()
            print('来了个新链接:',addr)
            inputs.append(conn)
            msg_dic[conn]=queue.Queue()#初始化一个队列实例，存要返回给这个客户端的数据
        else:
            data=r.recv(1024)  #这里应该写r，而不是conn，因为是可能你conn是第二个，但是收据来自第一个客户端
            print('收到数据:',data)
            msg_dic[r].put(data)
            outputs.append(r) #放入返回的链接队列里
            # r.send(data)
            # print('send done.....')
    for w in writeable:
        data_to_client=msg_dic[w].get()
        w.send(data_to_client)#返回给客户端源数据
        outputs.remove(w)  #删除这个链接，否则下次循环它还在里面
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)  #在outputs也删除它

        inputs.remove(e)  #它肯定在inputs里面
        del msg_dic[e]  #队列里的也删除

