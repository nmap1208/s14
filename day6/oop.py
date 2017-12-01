#Auther nmap
class Role(object):
    n=123   #类变量
    n_list=[]
    name='我是类name'
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        self.name=name
        self.role=role
        self.weapon=weapon
        self.life_valu=life_value
        self.money=money
    def shot(self):   #类的方法，功能（动态属性）
        print('shooting....')
    def got_shot(self):
        print('ah.....,I got shot...')
    def buy_gun(self,gun_name):
        print('just bought %s'%gun_name)
print(Role.n)
r1=Role('nmap','police','ak47')
r1.name='hehe'
r1.n='change n  by r1'
r1.n_list.append('from r1')
print(r1.n_list)
r2=Role('jack','terrorist','B22')
r2.name='haha'
r2.n_list.append('from r2')
print(Role.n)
print(r1.n,r1.name)
print(r2.n,r2.name)
print(r1.n_list)
print(r2.n_list)