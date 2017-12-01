#Auther nmap
import orm_many_fk
from  sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_many_fk.engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class() #生成session实例  #可以理解为打开游标cursor

# #准备插入数据
# add1=orm_many_fk.Address(street='tiantongyuan',city='changping',state='bj')
# add2=orm_many_fk.Address(street='wudaokou',city='haidian',state='bj')
# add3=orm_many_fk.Address(street='yanjiao',city='langfang',state='hb')
#
# Session.add_all([add1,add2,add3])
# c1=orm_many_fk.Customer(name='nmap1',billing_address=add1,shipping_address=add2)
# c2=orm_many_fk.Customer(name='nmap2',billing_address=add3,shipping_address=add3)
# Session.add_all([c1,c2])

#查询数据
obj=Session.query(orm_many_fk.Customer).filter(orm_many_fk.Customer.name=='nmap1').first()
print(obj.name,obj.billing_address,obj.shipping_address)
Session.commit()