#Auther nmap
import shelve
d=shelve.open('shelve_test')
info={'age':22,'job':'it'}
name=['nmap','rain','test']

d['name']=name
d['info']=info
d.close()