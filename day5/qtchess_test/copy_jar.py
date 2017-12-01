#Auther nmap
import os,sys
print(os.path.abspath(__file__))
JAR_DIR='D:\\0629\\myload'
print(JAR_DIR)
os.chdir(JAR_DIR)
print(os.listdir())
import shutil
ORI_FILE='D:\\0629\\myload\\ddz0\suite.jar'
for i in range(2,451):
    DST_DIR='D:\\0629\\myload\\ddz%s\\'%(str(i))
    #print(DST_DIR)
    shutil.copy(ORI_FILE,DST_DIR)
    print(os.listdir(DST_DIR))