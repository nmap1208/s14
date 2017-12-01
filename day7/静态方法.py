#Auther nmap
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def talk(self):
#         pass
#
#     @staticmethod
#     def animal_talk(obj):
#         obj.talk()
#
# class Cat(Animal):
#     def talk(self):
#         print('Meow!')
class Dog(object):
    #n=333
    name='lucy'
    def __init__(self,name):
        self.name=name

    # @staticmethod  #实际根类没什么关系了
    @classmethod
    def eat(self):
        print('%s is eating %s'%(self.name,'dd'))
    def talk(self):
        print('%s is talking '%self.name)

d=Dog('jack')
d.eat()

