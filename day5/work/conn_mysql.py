#Auther nmap
#coding=utf-8
import pymysql
conn = pymysql.connect(host="10.0.2.17",port=3306,user="dbuser",passwd="dbuser",db="dbuser",charset="utf8")
cur = conn.cursor()
f_sql=open('update_2','r',encoding='utf-8')
for line in f_sql:
    sql = line
    cur.execute(sql)
