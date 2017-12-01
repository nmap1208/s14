#Auther nmap
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from  sqlalchemy.orm import sessionmaker

Base = declarative_base() #生成orm基类
class User(Base):
    __tablename__ = 'user' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

engine = create_engine("mysql+pymysql://dbuser:1234@10.0.1.127/mydb",
                                    encoding='utf-8', echo=True)
Session_class = sessionmaker(bind=engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class() #生成session实例  #可以理解为打开游标cursor

user_obj1 = User(name="nmap",password="nmap123") #生成你要创建的数据对象
user_obj2 = User(name="nmap",password="nmap123") #生成你要创建的数据对象
print(user_obj1.name,user_obj1.id)  #此时还没创建对象呢，不信你打印一下id发现还是None

Session.add(user_obj1) #把要创建的数据对象添加到这个session里， 一会统一创建
Session.add(user_obj2) #把要创建的数据对象添加到这个session里， 一会统一创建
print(user_obj1.name,user_obj1.id) #此时也依然还没创建

Session.commit() #现此才统一提交，创建数据