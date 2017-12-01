#Auther nmap
import sys,os
print(sys.path)
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)
print(sys.path)
import module_name
module_name.sayhi()

