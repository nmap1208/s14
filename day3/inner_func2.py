# #Auther nmap
# print(bin(8))
# print(bool(3))
# print(bool(0))
# print(chr(97))
# print(hex(12))
# print(oct(12))
# set1=(1,2,3)
# print(sum(set1))
# print(range(1,11,2))

# a=bytes("abcde",encoding='utf-8')
# b=bytearray('abcde',encoding='utf-8')
# print(a.capitalize(),a)
# print(b[0])
# b[1]=100
# print(b)



#
# def sayhi():
#     pass
# print(callable(sayhi))

# code="for i in range(10):print(i)"
# exec(code)

# a=divmod(5,2)
# b=divmod(5,1)
# print(a)
# print(b)


# def sayhi(n):
#     print(n)
# sayhi(5)
#
# calc=lambda n:print(n)
# calc(5)
# print(filter(lambda n:n>5,range(10)))
# res=filter(lambda n:n>5,range(10))
# for i in res:
#     print(i)
#res=map(lambda n:n*2,range(10))
# res = [ lambda i:i*2 for i in range(10) ]
# for n in res:
#     x=res
#     print(x)
# import functools
# res=functools.reduce( lambda x,y:x+y,range(10))
# print(res)
# list1=[1,4,5]
# a=frozenset(list1)
# print(globals())
# def test():
#     local_var=333
#     print(locals())
#     print(globals())
# test()
# print(globals())
# print(globals().get('local_var'))
# a=round(1.3342)
# b=round(1.3342,2)
# print(a)
# print(b)
# a={
#     6:3,
#     2:5,
#     7:1
# }
# print(sorted(a.items()))
# print( sorted(a.items(),key=lambda x:x[1]) )
