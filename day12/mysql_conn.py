#Auther nmap
import pymysql

conn = pymysql.connect(host='10.0.1.127',user='dbuser',passwd='1234',db='mydb')

cur = conn.cursor()

reCount = cur.execute('insert into students(name,sex,age,tel) values("jack4","man",88,"67666");')
# reCount = cur.execute('insert into UserInfo(Name,Address) values(%(id)s, %(name)s)',{'id':12345,'name':'wupeiqi'})

conn.commit()

cur.close()
conn.close()

print (reCount)