#Auther nmap
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ahappier

import re


def main():
    a=input("请输入需要计算的公式：")
    b = "".join(a.split())
    while True:
        if "("in b:
            c = re.search(r"\([^()]+\)",b)
            if c is not None:
                e=c.group()
                d=cal(e)
                b=re.sub(r"\([^()]+\)",str(d),b,1)
        else:
            c=cal(b)
            print(c)
            break

#addition  and subtraction
def add_sub(b):

    if "--" in b:
        b=b.replace("--","+")
    add_list = re.findall(r"-?\d+\.?\d*", b)
    list=[]
    for i in add_list:
        list.append(float(i))
    t=sum(list)
    return t

#multiplication
def mul(b):
    mul_ch=re.search(r"\d+\.?\d*(\*-?\d+\.?\d*)",b)
    if mul_ch is not None:
        mul_ch=mul_ch.group()
        mul_list=re.findall(r"-?\d+\.?\d*",mul_ch)
        list=[]
        for i in mul_list:
            list.append(float(i))
        multip=list[0]*list[1]
        b=re.sub(r"\d+\.?\d*(\*-?\d+\.?\d*)",str(multip),b,1)
        return b

#division
def div(b):
    div_ch=re.search(r"\d+\.?\d*(\/-?\d+\.?\d*)",b)
    if div_ch is not None:
        div_ch=div_ch.group()
        div_list=re.findall(r"-?\d+\.?\d*",div_ch)
        list=[]
        for i in div_list:
            list.append(float(i))
        division=list[0]/list[1]
        b=re.sub(r"\d+\.?\d*(\/-?\d+\.?\d*)",str(division),b,1)
        return b

#calculation
def cal(c):
    while True:
        if "*"in c:
            s=c.split("*")
            if "/"in s[0]:
                c=div(c)
            else:
                c=mul(c)
        elif "/"in c:
            c=div(c)
        elif "+"or "-" in c:
            c=add_sub(c)
            return c
        else:
            return c

main()