#Auther nmap
import os,sys,subprocess
#os.system(r'"D:\0629\KEmulator\KEmulator.exe"  D:\0629\ddz1\suite.jar')
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
KE_EXE="D:\\0629\\myload\\KEmulator\\KEmulator.exe"
# KE_EXE="D:\\0629\\myload\\KEmulator\\KEmulator.exe"
# JAR_PATH="D:\\0629\\myload\\ddz1\\suite.jar"
# os.system(r'%s %s'%(KE_EXE,JAR_PATH))
