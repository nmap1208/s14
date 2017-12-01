#Auther nmap
import pymysql

conn = pymysql.connect(host='10.0.1.127',user='dbuser',passwd='1234',db='mydb')
cur = conn.cursor()
data=[
    ("lucy1","man",66,"87665"),
    ("lucy2","man",66,"87665"),
    ("lucy3","man",66,"87665"),
]
reCount = cur.executemany('insert into students(name,sex,age,tel) values(%s,%s,%s,%s)',data)
# reCount = cur.execute('insert into UserInfo(Name,Address) values(%(id)s, %(name)s)',{'id':12345,'name':'wupeiqi'})
conn.commit()

cur.close()
conn.close()

print (reCount)