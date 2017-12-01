#Auther nmap
from multiprocessing import Process, Queue
import threading,queue
def f(qq):
    qq.put([42, None, 'hello'])

if __name__ == '__main__':
    # q = Queue()
    q=queue.Queue()
    p = Process(target=f,args=(q,))
    # p=threading.Thread(target=f,args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()