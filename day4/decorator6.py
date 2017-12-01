#Auther nmap
import time
def consumer(name):
    print('%s 准备吃包子了' %name)
    while True:
        baozi=yield
        print(' %s 馅的包子来了,%s 把包子吃了' %(baozi,name))

# c=consumer('nmap')
# c.__next__()

# b1='韭菜馅'
# c.send(b1)

def producer(name):
    c=consumer('A')
    c2=consumer('B')
    next(c)
    next(c2)
    print('劳资开始做包子了')
    for i in range(10):
        time.sleep(1)
        print('做了2个包子')
        c.send(i)
        c2.send(i)

producer('nmap')
