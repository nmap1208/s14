#Auther nmap
from core import auth
from core import log
from core import transaction
from core import db_handle
from conf import setting
from core import accounts

import os
user_data={
    'account_id':None,
    'is_authenticated':False,
    'account_data':None

}

access_logger=log.log('access')
transaction_logger=log.log('transaction')


def account_info(access_data):
    print(access_data)

def repay(access_data):
    print(access_data)
    print('repay')
    account_data=accounts.load_account(access_data['account_id'])
    print(account_data)
    current_balance='''
    ---------Balance Info-----------
    Credit:%s
    Balance:%s

    '''%(account_data['credit'],account_data['balance'])
    back_flag=False
    while not back_flag:
        print(current_balance)
        repay_mount=input('\033[31;1mInput repay amount(b=back):\033[0m').strip()
        if len(repay_mount)>0 and repay_mount.isdigit():
            new_account_data=transaction.make_transaction(account_data,'repay',repay_mount,transaction_logger)
            if new_account_data:
                print('\033[42;1mNew Balance:%s\033[0m'%new_account_data['balance'])
        elif repay_mount=='b' or repay_mount=='back':
            back_flag=True
        else:
            print('\033[31;1m%s is not valid amount,Only accept interger!\033[0m'%(repay_mount))

def withraw(access_data):
    print(access_data)
    print('withraw')
    account_data=accounts.load_account(access_data['account_id'])
    print(account_data)
    current_balance='''
    ---------Balance Info-----------
    Credit:%s
    Balance:%s

    '''%(account_data['credit'],account_data['balance'])
    back_flag=False
    while not back_flag:
        print(current_balance)
        withdraw_amount=input('\033[31;1mInput withdraw amount(b=back);\033[0m').strip()
        if len(withdraw_amount)>0 and withdraw_amount.isdigit():
            new_accmount_data=transaction.make_transaction(account_data,'withdraw',withdraw_amount,transaction_logger)
            if new_accmount_data:
                print('\033[43;1mNew Balance:%s\033[0m'%new_accmount_data['balance'])
        elif withdraw_amount=='b' or withdraw_amount=='back':
            back_flag=True
        else:
            print('\033[31;1m%s is not valid amount,Only accept interger!\033[0m'%(withdraw_amount))

def transfer(access_data):
    print(access_data)
    print('withraw')
    account_data=accounts.load_account(access_data['account_id'])
    print(account_data)
    current_balance='''
    ---------Balance Info-----------
    Credit:%s
    Balance:%s

    '''%(account_data['credit'],account_data['balance'])
    back_flag=False
    while not back_flag:
        print(current_balance)
        transfer_amount=input('\033[31;1mInput withdraw amount(b=back);\033[0m').strip()
        if len(transfer_amount)>0 and transfer_amount.isdigit():
            new_accmount_data=transaction.make_transaction(account_data,'withdraw',transfer_amount,transaction_logger)
            if new_accmount_data:
                print('\033[43;1mNew Balance:%s\033[0m'%new_accmount_data['balance'])
        elif transfer_amount=='b' or transfer_amount=='back':
            back_flag=True
        else:
            print('\033[31;1m%s is not valid amount,Only accept interger!\033[0m'%(transfer_amount))


def paycheck(access_data):
    time=input('please input time(Y-M-D):')
    log_file='%s/logs/%s'%(setting.BASE_DIR,setting.LOGIN_TYPE['transaction'])
    print(log_file)
    with open (log_file,'r',encoding='utf-8') as f:
        for i in f.readlines():
            if time==i[0:10]:
                print(i)
            elif time==i[0:7]:
                print(i)
            elif time==i[0:4]:
                print(i)
def logout(access_data):
    q=input('if you want to quit,pls input q:')
    if q=='q':
        exit()

def interactive(access_data,**kargs):
    msg='''
        ---------------ICBC Band----------
        \033[31;1m
        1.账户信息
        2.存款
        3.取款
        4.转账
        5.账单
        6.退出
        \033[0m
        '''

    menu_dic={
        '1':account_info,
        '2':repay,
        '3':withraw,
        '4':transfer,
        '5':paycheck,
        '6':logout

    }

    flag=False
    while not flag:
        print(msg)
        choice=input('<<<:').strip()
        if choice in menu_dic:
            menu_dic[choice](access_data)
        else:
            print('\033[31;1mYou choice does not exist\033[0m' )
def run():
    access_data=auth.access_login(user_data,access_logger)
    print('AAAAA')
    if user_data['is_authenticated']:
        print('has authenticated')
        user_data['account_data']==access_data
        interactive(user_data)




























