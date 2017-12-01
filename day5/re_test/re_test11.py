#Auther nmap
import re
def main():
    data1=input("请输入要运算的公式:")
    data1=re.sub('\s','',data1)  #去掉空格
    #if re.search(r'\([^()]+\)',data1):
    while True:
        if '(' in data1:
            a1=re.search(r'\([^()]+\)',data1).group()
            c1=cal(a1)
            data1=re.sub(r'\([^()]+\)',str(c1),data1,count=1)
        else:
            data1=cal(data1)
            print(data1)
            break
def mul(b): #乘法
    m1=re.search(r"\d+\.?\d*\*-?\d+\.?\d*",b)
    #if m1 is not None:
    n1=m1.group()
    list1=re.findall(r'\-?\d+\.?\d*',n1)
    v1=float(list1[0])*float(list1[1])
    b=re.sub(r"\d+\.?\d*\*-?\d+\.?\d*",str(v1),b,count=1)
    return b
def div(b): #除法
    m1=re.search(r"\d+\.?\d*\/-?\d+\.?\d*",b)
    if m1 is not None:
        n1=m1.group()
        list1=re.findall(r'\-?\d+\.?\d*',n1)
        v1=float(list1[0])/float(list1[1])
        b=re.sub(r"\d+\.?\d*\/-?\d+\.?\d*",str(v1),b,count=1)
        return b
def add(str1): #加法
    if '--' in str1:
        str1=re.sub(r'--','+',str1)
    list1=re.findall(r'\-?\d+\.?\d*',str1)
    v1=0
    for i in list1:
        v1=v1+float(i)
    return v1

def cal(str1): #括号内的
    while True:
        if '*' in str1:
            list1=str1.split('*')
            if '/' in list1[0]:
                str1=div(str1)
            else:
                str1=mul(str1)
        elif '/' in str1:
            str1=div(str1)
        elif '+' or '-' in str1:
            str1=add(str1)
            return str1
        else:
            return str1

main()
