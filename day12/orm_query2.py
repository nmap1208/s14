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
class Students(Base):
    __tablename__ = 'students' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(8))
    sex = Column(String(4))
    age = Column(String(3))
    tel=Column(String(13))

    def __repr__(self):
        return "<%s name:%s>" %(self.id,self.name)

engine = create_engine("mysql+pymysql://dbuser:1234@10.0.1.127/mydb",
                                    encoding='utf-8', echo=False)
Session_class = sessionmaker(bind=engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class() #生成session实例  #可以理解为打开游标cursor
# print(Session.query(User,Students).filter(User.id==Students.id).all())
print(Session.query(User,Students).filter(User.id==Students.id).all())
Session.commit()
