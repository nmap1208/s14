#Auther nmap
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,num,sleep_time):
        threading.Thread.__init__(self)
        self.num=num
        self.sleep_time=sleep_time

    def run(self):
        print('running on number:%s'%self.num)
        time.sleep(self.sleep_time)

if __name__=='__main__':
    t1=MyThread(1,2)
    t2=MyThread(2,3)
    t1.start()
    t2.start()
    t1.join()  #它的作用是等待t1线程的返回结果，在获取结果之前，程序不往前走
    t2.join()
    print('main thread.......')