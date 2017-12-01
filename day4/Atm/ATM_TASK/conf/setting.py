#Auther nmap
import logging
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGIN_LEVEL=logging.INFO #定义日志的记录级别

DATABASE={
    'db_tool':'file_storage',
    'name':'accounts',
    'path':'%s/db' %(BASE_DIR)
}
#print(DATABASE)

LOGIN_TYPE={
    'access':'access.log',
    'transaction':'transaction.log'
}

TRANSACTION_TYPE={
    'repay':{'action':'plus','interest':0},
    'withdraw':{'action':'minus','interest':0.05},
    'transfer':{'action':'minus','interest':0}

}