#Auther nmap
#一本书可以有多个作者，一个作者又可以出版多本书


from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey,engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

#下面这种方式是采用的不常用的创建表的方式，这个是第三个表，书籍和作者关联的
book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books') #它是通过第三个表才能查找作者，因此有个secondary字段

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name

engine = create_engine("mysql+pymysql://dbuser:1234@10.0.1.127/mydb2?charset=utf8",
                                    encoding='utf-8', echo=False)
# Base.metadata.create_all(engine) #创建表结构