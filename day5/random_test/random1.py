#Auther nmap
import random
list1=[]
for i in range(10):
    list1.append(i)

random.shuffle(list1)
a=list1[0:4]
b=''
for i  in a:
    b+=str(i)
print(b)
print(type(b))