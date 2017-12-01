#Auther nmap
import re
data='1 - 2 * ( (60-30 +(-40/5) * (9--2*5/3 + 7 /3*99/4*2998 +-10 * 568/14 )) - (-4*3)/ (   16-3*2) )'
#去空格，方法1
# list1=data.split()
# data1=''.join(list1)
# print(data1)
# print(''.join(data1.split()))
# #去空格，方法3
# data1=re.sub('\s','',data)
# print(data1)
#去空格，方法2
# data1=data.replace(' ','')
# a1=re.search(r'\([^()]+\)',data).group()
# a2=re.search(r'(\d|\.|\+|\-|\*|\/)+',a1).group()
# print(a2)

data2='23*34-45*78/90'
def mul(str1): #乘法
    m1=re.search(r'\-?\d+\.?\d*\*\-?\d+\.?\d*',str1)
    if m1 is not None:
        n1=m1.group()
        list1=n1.split('*')
        v1=float(list1[0])*float(list1[1])
        str1=re.sub(r'\-?\d+\.?\d*\*\-?\d+\.?\d*',str(v1),str1,count=1)
    return str1
print(mul(data2))

