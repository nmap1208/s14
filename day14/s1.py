#Auther nmap
import socket

def handle_request(client):
    buf=client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n",encoding='utf-8'))
    f=open('index.html','r',encoding='utf-8')
    data=f.read()
    f.close()
    import time
    r=str(time.time())
    data=data.replace('@@@@@',r)
    client.send(bytes(data,encoding='utf-8'))
    client.close()

def main():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8000))
    sock.listen(5)

    while True:
        connection,address=sock.accept()
        handle_request(connection)
if __name__ == '__main__':
    main()
