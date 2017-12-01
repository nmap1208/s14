#Auther nmap
import os,sys,json,time

from core import db_handle
from conf import setting
from core import account

def access_auth(account_name,password):
    db_path=db_handle.handle(setting.DATABASE)
    account_file="%s/%s.json"%(db_path,account_name)
    if os.path.isfile(account_file):
        account_data=account.load_account(account_name)
        if password==account_data['password']:
            expire_time=time.mktime(time.strptime(account_data["expire_date"],"%Y-%m-%d"))
            if time.time()>expire_time:
                print('account %s has expired,pls contact the bank'%account_name)
                exit('exit for expired')
            else:
                print('login success')
                print(account_data)
                return account_data
        else:
            print('password not correct')
    print('account not exist')



def access_login(flag_data):
    retry=0
    while not flag_data['is_authenticated'] and retry<3:
        account_name=input('account_name:').strip()
        password=input('password:').strip()
        account_data=access_auth(account_name,password)
        if account_data:
            flag_data['is_authenticated']=True
            flag_data['account_name']=account_name
            print('welcome %s login'%account_name)
            return account_data
        retry+=1
    else:
        print("Account [%s] try logging too many times..." % account)
        exit('try too many times.....')







