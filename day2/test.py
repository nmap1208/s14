#Auther nmap
import copy
person=['name',['a',100]]
p1=person[:]
p2=person[:]
p1[0]='lisi'
p2[0]='xiaohong'
print(p1)
print(p2)
p1[1][1]=200
print(p1)
print(p2)
print(p1.index('lisi')+1)