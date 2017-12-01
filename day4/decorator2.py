#Auther nmap
#
# def bar():
#     print('in the bar')
# foo()
# def foo():
#     print('in the foo')
#     bar()


# def test():
#     pass
#
# test = '函数体'
# test()


# calc = lambda x:x*3
# print(calc)
# print(calc(3))

# def foo():
#     print('in the foo')
#     bar()
# foo()
# def bar():
#     print('in the bar')
# import time
# def bar():
#     time.sleep(2)
#     print('in the bar')
#
# def test1(func):
#     start_time=time.time()
#     func()
#     stop_time=time.time()
#     print('the func run time is %s' %(stop_time-start_time))
#
# test1(bar)


import time
def bar():
    time.sleep(2)
    print('in the bar')

def test2(func):
    print(func)
    return func

bar=test2(bar)
bar()