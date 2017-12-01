#Auther nmap
import os,sys
BASE_DIR=(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

DATABASE = {
    "db_tool":"file_storage",  #文件存储，这里可拓展成数据库形式的
    "name":"accounts",         #db下的文件名
    "path":"%s/db"%BASE_DIR
}
