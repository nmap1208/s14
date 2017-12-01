#Auther nmap
# print(__file__)  #它获取的其实是相对路径，因为pycharm的缘故，所以显示全了
import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #获取绝对路径
sys.path.append(BASE_DIR)
from conf import setting
from core import main
main.login()