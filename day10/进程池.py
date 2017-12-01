#Auther nmap
from  multiprocessing import Process,Pool,freeze_support
import time,os

def Foo(i):
    time.sleep(2)
    print('foo...pid',os.getpid())
    return i+100

def Bar(arg):
    print('-->exec done:',arg,'bar...pid:',os.getpid())

if __name__ == '__main__':  #它的作用是为了区分你是主动执行这个脚本，还是在别的地方把它当一个模块调用
    # freeze_support()
    print('current..pid',os.getpid())
    pool = Pool(5)

    for i in range(10):
        pool.apply_async(func=Foo, args=(i,),callback=Bar)
        # pool.apply(func=Foo, args=(i,))

    print('end')
    pool.close()
    pool.join()#进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。