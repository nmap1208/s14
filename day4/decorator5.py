#Auther nmap
def fib(max):
    n,a,b=0,0,1
    while n<max:
        a,b=b,a+b
        yield b
        n+=1
    return 'done'

g = fib(5)
while True:
    try:
        x=next(g)
        print(x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


