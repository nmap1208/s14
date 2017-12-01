#Auther nmap
import os,sys,json
from core import db_handle
from conf import setting

def load_account(account_name):
    db_path=db_handle.handle(setting.DATABASE)
    account_file="%s/%s.json"%(db_path,account_name)
    with open(account_file,'r',encoding='utf-8') as f:
        account_data=json.load(f)
        return account_data


def dump_account(account_data):
    db_path=db_handle.handle(setting.DATABASE)
    account_file="%s/%s.json"%(db_path,account_data['id'])
    with open(account_file,'w+',encoding='utf-8') as f:
        json.dump(account_data, f)
    print('dump success')

