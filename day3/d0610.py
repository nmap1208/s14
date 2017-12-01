#Auther nmap
# -*- coding: utf-8 -*-
import re
a='''xingmin: zhang
shuju: 197
xuexiao: xi
'''
b=re.search(r"(?<=shuju:).+?(?=$)",a,re.M)
print(b.group(0))