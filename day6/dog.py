#Auther nmap
class Dog:
    def __init__(self,name):
        self.name=name

    def bulk(self):
        print('%s:wang wang wang' %self.name)

d1=Dog('旺财')
d2=Dog('小黑')
d3=Dog('哈士奇')
d1.bulk()
d2.bulk()
d3.bulk()
