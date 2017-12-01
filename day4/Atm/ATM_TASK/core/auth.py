#Auther nmap
import os
import sys
import time
from core import accounts
from core import db_handle
from conf import setting

def access_auth(account,password,log_obj):
    db_path=db_handle.handle(setting.DATABASE)
    print(db_path)
    account_file='%s/%s.json'%(db_path,account)
    if os.path.isfile(account_file):
        account_data=accounts.load_account(account)
        print(account_data)
        if account_data['password']==password:
            expire_time=time.mktime(time.strptime(account_data['expire_date'],'%Y-%m-%d'))
            if time.time()>expire_time:
                log_obj.error('Account %s had expired,pls contach the bank'%(account))
                print('Account %s had expired,pls contach the bank'%(account))
            else:
                log_obj.info('Account %s logging success'%(account))
                return account_data
        else:
            log_obj.error('Account or  Password does not correct!')
            print('Account or  Password does not correct!')


    else:
        log_obj.error('Account %s does not exist'%(account))
        print('Account %s does not exist'%(account))

def access_login(user_data,log_obj):
    retry=0
    while not user_data['is_authenticated'] and retry<3:
        account=input('Account>>>:').strip()
        password=input('Password>>>:').strip()
        user_auth_data=access_auth(account,password,log_obj)

        if user_auth_data:
            user_data['is_authenticated']=True
            user_data['account_id']=account
            print('welcome %s' %(account))
            return user_auth_data
        retry +=1
    else:
        print('Account %s try logging too  many times...'%account)
        log_obj.error('Account %s try logging too  many times...'%account)
        exit()
