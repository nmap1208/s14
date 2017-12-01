#Auther nmap
import os,sys
print(os.path.abspath(__file__))
JAR_DIR='D:\\0629\\myload'
ORI_JAD='D:\\0629\\myload\\ddz0\suite.jad'
os.chdir(JAR_DIR)
print(os.listdir())
f_str=open(ORI_JAD,'r',encoding='utf-8')
jad_list=f_str.readlines()
begin_str=jad_list[11].split(':')[0]
numbercode=int(jad_list[11].split(':')[1].strip())
for i in range(1,451):
    tmp_code=numbercode+i
    tmp_str=begin_str+': '+str(tmp_code)+'\n'  #开始拼接字符串,原来字符串最后带换行符，因此这里也要加上
    jad_list[11]=tmp_str
    tmp_jad=open('D:\\0629\\myload\\ddz%s\suite.jad'%i,'w',encoding='utf-8')
    for line in jad_list:
        tmp_jad.write(line)
    tmp_jad.close()

