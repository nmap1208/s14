#Auther nmap
import queue
import threading
import time

q=queue.Queue(maxsize=10)

def Producer(name):
    count=1
    while True:
        q.put('骨头%s'%count)
        print('生产了骨头',count)
        count+=1
        time.sleep(0.5)

def Consumer(name):
        # while q.qsize()>0:
        while True:
            print('%s 取到了 %s,并且吃了它。。。。'%(name,q.get()))
            time.sleep(1)
p=threading.Thread(target=Producer,args=('nmap',))
c=threading.Thread(target=Consumer,args=('sam',))
c1=threading.Thread(target=Consumer,args=('tom',))
p.start()
c.start()
c1.start()