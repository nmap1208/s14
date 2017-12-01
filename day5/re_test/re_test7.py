#Auther nmap
import re
def jjcc(str1):  #表示加减乘除
    str1=re.sub('\s','',str1) #去掉空格
    str1=re.sub('\-\-','+',str1) #两个连续的减号变成加号
    str1=re.sub('\+\-','-',str1) #连续的加减符号等于减号
    return str1
data='1 - 2 * ( (60-30 +(--40/5) * (9--2*5/3 + 7 /3*99/4*2998 +-10 * 568/14 )) - (-4*3)/ (16-3*2) )'


data2='3/-2-1/-2'

def c_j(data_1):
    def chujia():
            if re.search('(\d|\.)+(\/\-)(\d|\.)+',data_1):
                c=re.search('(\d|\.)+(\/\-)(\d|\.)+',data_1).group()
                c='-'+re.sub('\/\-','/',c)
                return c
    while True:
        ori=re.search('(\d|\.)+(\/\-)(\d|\.)+',data_1).group()
        print(ori)
        n_v=chujia()
        print(n_v)
        data_2=re.sub(ori,chujia(),data_1)
        return data_2

print(c_j(data2))


