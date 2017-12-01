#Auther nmap
import re,time,copy
data='1-32/4*2+3*6/2+5'
def calc(str1):
    print('str1:',str1)
    v1=eval(str1)
    return str(v1)

def chengchu(str1):
    pass


def no_space(data):         #去掉空格
    data=re.sub('\s','',data)
    return data

def jianjian(data):         #两个连续的减号变成加号
    data=re.sub('\-\-','+',data)
    return data

def jiajian(data):      #连续的加减符号等于减号
    data=re.sub('\+\-','-',data)
    return data

def chengjian():
    data=re.sub('(\d\.)+\*\-(\d\.)+','-()')

def jjcc(data):  #表示加减乘除


    d

    while data:
        print('current data:',data)
        if re.search('(\d|\.)+(\*|\/)(\d|\.)+',data):   #匹配乘除 ，适用于-5*2,不适用于-5*-2  肯定要有括号的
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