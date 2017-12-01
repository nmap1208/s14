#Auther nmap
import pymysql

conn = pymysql.connect(host='10.0.1.127',user='dbuser',passwd='1234',db='mydb')
cur = conn.cursor()
cur.execute("select * from students")
# 获取第一行数据
row_1 = cur.fetchone()
# 获取前n行数据
row_2 = cur.fetchmany(3)
# 获取剩余所有数据
row_3 = cur.fetchall()

conn.commit()
cur.close()
conn.close()
print('row_1:',row_1)
print('row_2:',row_2)
print('----------------')
print('row_3:',row_3)