#Auther nmap
class Dog(object):

    def __init__(self,name,food):
        self.name=name
        self.__food=None

    @property
    def eat(self):
        print('%s is eating %s'%(self.name,self.__food))

    @eat.setter
    def eat(self,food):
        print('set to food',food)
        self.__food=food
    @eat.deleter
    def eat(self):
        del self.__food
        print('删除完了')

    def talk(self):
        print('%s is talking '%self.name)

d=Dog('jack','apple')
d.eat
d.eat='baozi'
d.eat
del d.eat
d.eat
