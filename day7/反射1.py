#Auther nmap
def bulk(self):
    print('%s is yelling......'%self.name)

class Dog(object):
    def __init__(self,name):
        self.name=name
    def eat(self,food):
        print('%s is eating....%s'%(self.name,food))
d=Dog('jack')
choice=input('>>:').strip()
if hasattr(d,choice):
    func=getattr(d,choice)
    func('apple')
else:
    setattr(d,choice,bulk)  #d.talk=bulk
    func=getattr(d,choice)
    func(d)