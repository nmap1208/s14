#Auther nmap
import os,sys
print(os.path.abspath(__file__))
JAR_DIR='D:\\0629\\myload'
print(JAR_DIR)
os.chdir(JAR_DIR)
print(os.listdir())
def create_dir(start_num,stop_num):
    for i in range(start_num,stop_num):
        tmp_dir='ddz'+str(i)
        #print(tmp_dir)
        os.mkdir(tmp_dir)
    print(os.listdir())

create_dir(1,451)

