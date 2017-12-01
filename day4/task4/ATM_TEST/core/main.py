#Auther nmap
from core import auth
from core import account
import os


flag_data={
    'account_name':None,
    'is_authenticated':False,
    'account_data':None
}


def account_info(access_data):
    print('account_info')
    print(access_data)
def repay(access_data):
    print('repay')
    return access_data
def withdraw(access_data):
    print('withdraw')
    return access_data
def transfer(access_data):
    print('transfer')
    return access_data
def paycheck(access_data):
    print('paycheck')
    return access_data
def freeze_account(access_data):
    print('freeze_account')
    return access_data
def logout(access_data):
    print('logout')
    return access_data

def interactive(access_data):
    print('start interactive')
    msg='''
#################菜单功能##################
1. 查看账户信息
2. 还款
3. 取钱
4. 转账
5. 查看账单
6. 冻结账户
7. 退出
#################--end--###################
'''

    menu_dict={
        '1':account_info,
        '2':repay,
        '3':withdraw,
        '4':transfer,
        '5':paycheck,
        '6':freeze_account,
        '7':logout
    }
    print(msg)
    choice=input('pls enter a  number to have a choice:')
    #if choice.isdigit():
        #choice=int(choice)
    if choice in menu_dict:
        menu_dict[choice](access_data)





def run():
    access_data=auth.access_login(flag_data)
    print('hello')
    if access_data:
        print('welcome login')
        interactive(access_data)
    else:
        print('username or passwd not correct,fuck out')
        exit()