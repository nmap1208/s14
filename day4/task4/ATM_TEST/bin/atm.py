#Auther nmap
import os,sys

BASE_DIR=(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,BASE_DIR)
print(BASE_DIR)
print(os.listdir(BASE_DIR))

from core import main
if __name__ == '__main__':
    main.run()