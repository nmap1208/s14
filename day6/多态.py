#Auther nmap
class Animal(object):
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

    def func(ob): #一个接口，多种形态
        ob.talk()

class Cat(Animal):
    def talk(self):
        print('%s: 喵喵喵!' %self.name)


class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' %self.name)

c1 = Cat('小晴')
d1 = Dog('李磊')

Animal.func(c1)
Animal.func(d1)