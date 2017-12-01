#Auther nmap
class Role(object):
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        self.name=name
        self.role=role
        self.weapon=weapon
        self.__life_value=life_value
        self.money=money
    def __shot(self):
        pass
    def buy_gun(self,gun_name):
        print('%s 购买了%s'%(self.name,gun_name))
    def got_shot(self):
        self.__life_value-=50
        print('%s中枪了....'%self.name)
    def __del__(self):
        print('%s 彻底死了...'%self.name)
    def show_status(self):
        print('name:%s weapon:%s life_val:%s'%(self.name,
                                               self.weapon,
                                               self.__life_value))
p1=Role('nmap','police','ak47')
p1.buy_gun('B25')
p1.got_shot()
print(p1.role)
p1.show_status()
p1.shot()