#Auther nmap
import orm_m2m
from  sqlalchemy.orm import sessionmaker
#插入数据
Session_class = sessionmaker(bind=orm_m2m.engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class() #生成session实例  #可以理解为打开游标cursor

# b1 = orm_m2m.Book(name="book1")
# b2 = orm_m2m.Book(name="book2")
# b3 = orm_m2m.Book(name="book3")
# b4 = orm_m2m.Book(name="book4")
b5 = orm_m2m.Book(name="book4哈哈哈")
# a1 = orm_m2m.Author(name="nmap")
# a2 = orm_m2m.Author(name="Jack")
# a3 = orm_m2m.Author(name="Rain")
#
# b1.authors = [a1,a2]
# b2.authors = [a1,a2,a3]
# Session.add_all([b1,b2,b3,b4,a1,a2,a3])
Session.add_all([b5,])
# print('--------通过书表查关联的作者---------')
#
# book_obj = Session.query(orm_m2m.Book).filter(orm_m2m.Book.name=="book1").first()
# print(book_obj)
# print(book_obj.name, book_obj.authors)
#
# print('--------通过作者表查关联的书---------')
# author_obj =Session.query(orm_m2m.Author).filter(orm_m2m.Author.name=="nmap").first()
# print(author_obj.name , author_obj.books)
# book_obj.authors.remove(author_obj)
# Session.delete(author_obj)
Session.commit()
