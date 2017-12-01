#Auther nmap
import threading
import time

def sayhi(num):
    print('running on number:%s' %num)
    time.sleep(3)

if __name__=='__main__':
    t1=threading.Thread(target=sayhi,args=(1,)) #生成一个实例
    t2=threading.Thread(target=sayhi,args=(2,))

t1.start()
t2.start()

print(t1.getName())  #获取线程名
print(t2.getName())