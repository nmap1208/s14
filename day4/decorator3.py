#Auther nmap
# def foo():
#     print('in the foo')
#     def bar():
#         print('in the bar')
#     bar()
#
# foo()
# import time
# def timer(func):
#     def deco():
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print('the func run time is %s' %(stop_time-start_time))
#     return deco
# @timer
# def test1():
#     time.sleep(2)
#     print('in the test1')
# @timer          # test2= timer(test2) =deco  test2()=deco()
# # def test2(name):
# #     time.sleep(2)
# #     print('test2',name)
# # test1()
# # test2()
# import time
# def timer(func):
#     def deco(arg1,arg2):
#         start_time=time.time()
#         func(arg1,arg2)
#         stop_time=time.time()
#         print('the func run time is %s' %(stop_time-start_time))
#     return deco
# # @timer
# # def test1():
# #     time.sleep(2)
# #     print('in the test1')
# @timer          # test2= timer(test2) =deco  test2()=deco()
# def test2(name,age):
#     time.sleep(2)
#     print('test2',name,age)
# test2('nmap',22)
import time
def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return warpper
@timmer
def test1():
    time.sleep(2)
    print('in the test1')
# @timmer        # test2= timer(test2) =deco  test2()=deco()
# def test2(name,age):
#     time.sleep(2)
#     print('test2',name,age)
test1()
# test2('nmap',22)