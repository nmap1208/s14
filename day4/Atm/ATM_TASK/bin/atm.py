#Auther nmap
import  os
import sys
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,dir)
print(dir)
print(sys.path)

#将main.py里面所有代码封装成main变量
from core import main

if __name__=='__main__':
    main.run()

