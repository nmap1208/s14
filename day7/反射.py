#Auther nmap


def bulk(self):
    print('%s is yelling....'%self.name)

class Dog(object):

    def __init__(self,name):
        self.name=name
    def eat(self,food):
        print('%s is eating %s'%(self.name,food))

d=Dog('jack')
choice =input('>>:')
if hasattr(d,choice):
    delattr(d,choice)
    # func=getattr(d,choice)
    # func('apple')
    # attr=getattr(d,choice)
    # setattr(d,choice,'lily')
else:
    # setattr(d,choice,bulk)
    # d.talk(d)
    setattr(d,choice,22)
    print(getattr(d,choice))
print(d.name)