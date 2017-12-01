##Auther nmap
#a={1,2,3,4}
#b={3,4,5,6}
#c={1,2,3,5,4,6,7}
#print(type(a))   #打印a的类型
#print(a.difference(b)) #打印a中，减去a和b的交集
#print(a.union(b))   #a并b
#print(a.symmetric_difference(b))   #打印a和b的并集，去掉a和b的交集,对称差集
#print(a.issubset(b))    #判断a是否是b的子集
#print(a.issubset(c))    #判断a是否是c的子集
#print(a.issuperset(b))    #判断a是否是b的父集
#print(a.intersection(b))  #打印a和b的交集
#
#####集合去重
#d=[1,2,3,4,5,1,2,3]
#e=set(d)
#print(e)

f={1,2,3}
g={4,5,6}
print(f.discard({1,2}))
print(f)
f.discard(1)
print(f)
print(f.discard(4))
print(f)