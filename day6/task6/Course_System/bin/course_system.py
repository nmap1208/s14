#Auther nmap
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #获取绝对路径
sys.path.append(BASE_DIR)
# from conf import setting
from core import main
main.inter()