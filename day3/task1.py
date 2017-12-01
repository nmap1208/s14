#Auther nmap
import sys
def select(*args):
    print(args)
    a=args[0]
    a=str(a)
    print(a)
    d=a.split()
    print(d)

select('select name from tab1 where id > 20')