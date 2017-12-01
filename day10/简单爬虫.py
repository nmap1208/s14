#Auther nmap
from urllib import request

def f(url):
    print('get: %s'%url)
    resp=request.urlopen(url)
    data=resp.read()
    f=open('url html','wb')
    f.write(data)
    f.close()
    print('%d bytes recived from %s'%(len(data),url))

f('http://10.0.1.12')