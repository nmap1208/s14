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

    def __repr__(self):
        return "<%s name:%s>" %(self.id,self.name)

engine = create_engine("mysql+pymysql://dbuser:1234@10.0.1.127/mydb",
                                    encoding='utf-8', echo=False)
Session_class = sessionmaker(bind=engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class() #生成session实例  #可以理解为打开游标cursor
# my_user = Session.query(User).filter(User.id==1).all()
my_user1 = Session.query(User).filter_by(name="nmap").first()
my_user2 = Session.query(User).filter_by(name="nmap").all()
# my_user.name='jack'
# Session.add(my_user)
# Session.commit()
# my_user = Session.query(User).filter(User.id==1).first()
print('type of my_user1_first:',type(my_user1))
print('type of my_user2_all:',type(my_user2))
# print(my_user.id,my_user.name)