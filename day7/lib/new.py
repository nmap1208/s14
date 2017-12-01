#Auther nmap
# class Foo(object):
#
#     def __init__(self,name):
#         self.name = name
#
# f = Foo("nmap")
# print (type(f)) # 输出：<class '__main__.Foo'>   表示，obj 对象由Foo类创建
# print (type(Foo)) # 输出：<type 'type'>      表示，Foo类对象由 type 类创建
# class Foo(object):
#
#     def func(self):
#         print ('hello nmap')
#
# def func(self):
#     print ('hello nmap2')
#
# Foo = type('Foo',(object,), {'func': func})
# #type第一个参数：类名
# #type第二个参数：当前类的基类
# #type第三个参数：类的成员
def func(self):
    print("hello %s"%self.name)

def __init__(self,name,age):
    self.name = name
    self.age = age
Foo = type('Foo',(object,),{'func':func,'__init__':__init__})

f = Foo("jack",22)
f.func()