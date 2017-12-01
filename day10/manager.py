#Auther nmap
from multiprocessing import Process, Manager
import os
def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(os.getpid()) #放自己的进程号
    print(l)

if __name__ == '__main__':
    with Manager() as manager:  #实例化一个Manager()，等同于manager=Manager()
        d = manager.dict()   #可以被共享的字典

        l = manager.list(range(5))#可以被共享的列表
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)