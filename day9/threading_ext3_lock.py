#Auther nmap
import threading
import time

num=0
lock=threading.Lock()  #实例化一个线程锁

def run(n):
    lock.acquire()  #获取锁
    global  num
    num+=1
    time.sleep(1)
    lock.release()  #释放锁

t_objs=[]
starttime=time.time()
for i in range(50):
    t=threading.Thread(target=run,args=('t-%s'%i,))
    t.start()
    t_objs.append(t)

for t in t_objs:
   t.join()

print('all threading finished....')
print('num:',num)