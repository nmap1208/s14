#Auther nmap
import shelve
d=shelve.open('shelve_test')
print(d.get('name'))
print(d.get('info'))
