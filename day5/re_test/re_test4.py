#Auther nmap
import re,time,copy
data='1-32/4*2+3*6/2+5'
def calc(str1):
    print('str1:',str1)
    v1=eval(str1)
    return str(v1)

def chengchu(str1):
    pass
while data:
    print('current data:',data)
    if re.search('(\d|\.)+(\*|\/)(\d|\.)+',data):   #匹配乘除
        c=re.search('(\d|\.)+(\*|\/)(\d|\.)+',data)
        c_str=c.group()
        print('乘除计算str:',c_str)
        c_v=calc(c_str)
        c_str=re.sub('\*','\\\*',c_str)  #把乘以号*替换为\*,这里不转移的话会匹配不上
        print(c_str)
        data=re.sub(c_str,c_v,data)
        print('data:',data)
    elif re.search('(-)?(\d|\.)+(\+|\-)(\d|\.)+',data):#匹配加减
        c=re.search('(-)?(\d|\.)+(\+|\-)(\d|\.)+',data)
        c_str=c.group()
        print('加减计算str:',c_str)
        c_v=calc(c_str)
        print('当前:',c_v)
        c_str=re.sub('\+','\\\+',c_str)  #把加号+替换为\+,这里不转移的话会匹配不上
        print(c_str)
        data=re.sub(c_str,c_v,data)
        print('data:',data)
    else:
        exit()
# str1='8.0*2'
# print(eval(str1))
# data='1-8.0*2+5'
# print(re.search('(\d|\.)+(\*|\/)(\d|\.)+',data))
# print(re.search('(\d|\.)+(\*|\/)(\d|\.)+',data).group())
# c=re.search('(\d|\.)+(\*|\/)(\d|\.)+',data).group()
# d=copy.deepcopy(c)
# c_v=eval(d)
# c_v=str(c_v)
# print(c_v)
# print(re.search('8.0\*2',data))
