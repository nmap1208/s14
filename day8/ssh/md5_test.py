#Auther nmap
import hashlib
m=hashlib.md5()
m.update('abc'.encode())
m.update('def'.encode())
print(m.hexdigest())

n=hashlib.md5()
n.update('abcdef'.encode())
print(n.hexdigest())