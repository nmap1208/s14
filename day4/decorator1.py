#Auther nmap
# import time
# def timmer(func):
#     def warpper(*args,**kwargs):
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print('the func run time is %s' %(stop_time-start_time))
#     return warpper
#
# @timmer
# def test1():
#     time.sleep(3)
#     print('in the test1')
#
#
# test1()
import time
def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('the func run time is %s' %(stop_time-start_time))
        return res
    return warpper

@timmer
def test1(name):
    time.sleep(1)
    print('in the test1' ,name)
    return 'ok'

print(test1('name2'))
