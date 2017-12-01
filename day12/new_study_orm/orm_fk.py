#Auther nmap
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATE,ForeignKey
from  sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base() #生成orm基类
engine = create_engine("mysql+pymysql://dbuser:1234@10.0.1.127/mydb2",
                                    encoding='utf-8', echo=False)
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
    name = Column(String(32),nullable=False)
    register_date = Column(DATE,nullable=False)

    def __repr__(self):
        return "<%s name:%s>" %(self.id,self.name)
class StudyRecord(Base):
    __tablename__ ='study_record'
    id = Column(Integer, primary_key=True)
    day=Column(Integer,nullable=False)
    status=Column(String(32),nullable=False)
    user_id = Column(Integer, ForeignKey('students.id'))

    students = relationship("Students", backref="my_study_record") #这个nb，允许你在students表里通过backref字段反向查出所有它在students表里的关联项
    def __repr__(self):
        return "<%s day:%s status:%s>" %(self.students.name,self.day,self.status)
Base.metadata.create_all(engine) #创建表结构


#插入数据

Session_class = sessionmaker(bind=engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class() #生成session实例  #可以理解为打开游标cursor
# #创建学员
# s1=Students(name='nmap1',register_date='2017-09-11')
# s2=Students(name='nmap2',register_date='2017-09-12')
# s3=Students(name='nmap3',register_date='2017-09-13')
# s4=Students(name='nmap4',register_date='2017-09-14')
#
# #创建上课记录
# study_obj1=StudyRecord(day=1,status='YES',user_id=1)
# study_obj2=StudyRecord(day=2,status='NO',user_id=1)
# study_obj3=StudyRecord(day=3,status='YES',user_id=1)
# study_obj4=StudyRecord(day=1,status='YES',user_id=2)
#
# #批量创建
# Session.add_all([s1,s2,s3,s4,study_obj1,study_obj2,study_obj3,study_obj4])
stu_obj=Session.query(Students).filter(Students.name=='nmap1').first()
print(stu_obj)
print(stu_obj.my_study_record)
Session.commit()


