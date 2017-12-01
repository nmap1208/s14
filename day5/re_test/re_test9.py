#Auther nmap
#Auther nmap
import re
def jjcc(str1):  #表示加减乘除
    str1=re.sub('\s','',str1) #去掉空格
    str1=re.sub('\-\-','+',str1) #两个连续的减号变成加号
    str1=re.sub('\+\-','-',str1) #连续的加减符号等于减号
    return str1
data='1 - 2 * ( (60-30 +(--40/5) * (9--2*5/3 + 7 /3*99/4*2998 +-10 * 568/14 )) - (-4*3)/ (16-3*2) )'


data2='3*-2-1*-2/-2/-2'

def chengjian(data_1):
        if re.search(r'(\d|\.)+(\*\-)(\d|\.)+',data_1):
            c=re.search(r'(\d|\.)+(\*\-)(\d|\.)+',data_1).group()
            c='-'+re.sub(r'\*\-',r'*',c)
            return c
def chujian(data_1):
        if re.search(r'(\d|\.)+(\/\-)(\d|\.)+',data_1):
            c=re.search(r'(\d|\.)+(\/\-)(\d|\.)+',data_1).group()
            c='-'+re.sub(r'\/\-',r'/',c)
            return c
def cheng_jian(data_1):
    # def chengjia():
    #         if re.search(r'(\d|\.)+(\*\-)(\d|\.)+',data_1):
    #             c=re.search(r'(\d|\.)+(\*\-)(\d|\.)+',data_1).group()
    #             c='-'+re.sub(r'\*\-',r'*',c)
    #             return c
    while re.search(r'(\d|\.)+(\*\-)(\d|\.)+',data_1) is not None :
        # ori=re.search(r'(\d|\.)+(\*\-)(\d|\.)+',data_1).group()
        # print(ori)
        n_v=chengjian(data_1)
        # print(n_v)
        data_1=re.sub(r'(\d|\.)+(\*\-)(\d|\.)+',n_v,data_1)
        return data_1

def chu_jian(data_1):
    while re.search(r'(\d|\.)+(\/\-)(\d|\.)+',data_1) is not None :
        n_v=chujian(data_1)
        # print(n_v)
        data_1=re.sub(r'(\d|\.)+(\/\-)(\d|\.)+',n_v,data_1)
        return data_1
# data2='3*-2-1*-2'
# print(re.sub(r'3\*-2','-3*2',data2))
print(data2)
print(cheng_jian(data2))  #可以判断，上面是None时才停止
data2_1=cheng_jian(data2)
print(chu_jian(data2_1))