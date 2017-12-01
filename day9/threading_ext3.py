#Auther nmap
import threading
import time

def run(n):
    print('task',n)
    time.sleep(2)
    print('task done',n)
t_objs=[]
starttime=time.time()
for i in range(50):
    t=threading.Thread(target=run,args=('t-%s'%i,))
    t.setDaemon(True)  #把当前线程变成守护线程，一定要在start之前
    t.start()
    t_objs.append(t)
print('active thread:',threading.active_count())
# for t in t_objs:
#     t.join()

print('----------all threads has finished....',threading.current_thread())

print('cost:',time.time()-starttime)
