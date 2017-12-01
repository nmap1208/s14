#Auther nmap
"""
主逻辑交互模块
"""
from core import auth
from core import log
from core import transaction
from core import account
from conf import settings
from core import db_handle

import os


#用户数据信息
user_data = {
    'account_id':None,          #帐号ID
    'is_authenticated':False,  #是否认证
    'account_data':None        #帐号数据

}

#调用log文件下的log方法，返回日志对象
access_logger = log.log("access")
transaction_logger = log.log("transaction")



def account_info(access_data):
    """
    access_data:包括ID，is_authenticaed,用户帐号信息
    查看用户帐户信息
    :return:
    """
    print(access_data)




def repay(access_data):
    """
    access_data:包括ID，is_authenticaed,用户帐号信息
    还款
    :return:
    """
    print(access_data)
    print("repay")
    #调用account模块的load_account方法，从数据库从load出用户信息
    account_data = account.load_account(access_data["account_id"])
    print(account_data)
    current_balance = """
    -------------BALANCE INFO--------------
    Credit:%s
    Balance:%s
    """ % (account_data["credit"], account_data["balance"])
    back_flag = False
    while not back_flag:
        print(current_balance)
        repay_amount = input("\033[31;1mInput repay amount(b=back):\033[0m").strip()
        #如果用户输入整型数字
        if len(repay_amount) > 0 and repay_amount.isdigit():
            #调用transaction模块的方法,参数分别是用户帐户信息，交易类型，交易金额
            new_account_data = transaction.make_transaction(account_data, "repay", repay_amount,transaction_logger)
            if new_account_data:
                print("\033[42;1mNew Balance:%s\033[0m" % new_account_data["balance"])

        else:
            print("\033[31;1m%s is not valid amount,Only accept interger!\033[0m" % repay_amount)

        if repay_amount =="b" or repay_amount == "back":
            back_flag = True

def withdraw(access_data):
    """
    取款
    :return:
    """
    print(access_data)
    print("withdraw")
    # 调用account模块的load_account方法，从数据库从load出用户信息
    account_data = account.load_account(access_data["account_id"])
    print(account_data)
    current_balance = """
       -------------BALANCE INFO--------------
       Credit:%s
       Balance:%s
       """ % (account_data["credit"], account_data["balance"])
    back_flag = False
    while not back_flag:
        print(current_balance)
        withdraw_amount = input("\033[31;1mInput withdraw amount(b=back):\033[0m").strip()
        # 如果用户输入整型数字
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            # 调用transaction模块的方法,参数分别是用户帐户信息，交易类型，交易金额
            new_account_data = transaction.make_transaction(account_data, "withdraw", withdraw_amount,transaction_logger)
            if new_account_data:
                print("\033[42;1mNew Balance:%s\033[0m" % new_account_data["balance"])

        else:
            print("\033[31;1m%s is not valid amount,Only accept interger!\033[0m" % withdraw_amount)

        if withdraw_amount == "b" or withdraw_amount == "back":
            back_flag = True


def transfer(access_data):
    """
    转帐
    :return:
    """
    print(access_data)
    print("transfer")
    # 调用account模块的load_account方法，从数据库从load出用户信息
    account_data = account.load_account(access_data["account_id"])
    print(account_data)
    current_balance = """
           -------------BALANCE INFO--------------
           Credit:%s
           Balance:%s
           """ % (account_data["credit"], account_data["balance"])
    back_flag = False
    while not back_flag:
        print(current_balance)
        transfer_amount = input("\033[31;1mInput transfer amount(b=back):\033[0m").strip()
        # 如果用户输入整型数字
        if len(transfer_amount) > 0 and transfer_amount.isdigit():
            # 调用transaction模块的方法,参数分别是用户帐户信息，交易类型，交易金额
            new_account_data = transaction.make_transaction(account_data, "transfer", transfer_amount,transaction_logger)
            if new_account_data:
                print("\033[42;1mNew Balance:%s\033[0m" % new_account_data["balance"])
            new_account_data2 = transaction.make_transaction(account_data, "repay", new_account_data["balance"],transaction_logger)
            if new_account_data2:
                print("\033[42;1mNew Balance2:%s\033[0m" % new_account_data2["balance"])

        else:
            print("\033[31;1m%s is not valid amount,Only accept interger!\033[0m" % transfer_amount)

        if transfer_amount == "b" or transfer_amount == "back":
            back_flag = True


def paycheck(access_data):
    """
    账单查看
    :return:
    """

    time=input("please input time（Y-M-D）:")
    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOGIN_TYPE["transaction"])
    print(log_file)
    with open (log_file,"r",encoding="utf-8") as f :
        for i in f.readlines():
            if time == i[0:10]:
                print(i)
            elif time == i[0:7]:
                print(i)
            elif time == i[0:4]:
                print(i)




def logout(access_data):
    """
    退出登陆
    :return:
    """
    q = input("If you want to quit,please input q:")
    if q =="q":
        exit()


def interactive(access_data,**kwargs):
    """
    用户交互
    :return:
    """
    msg = (
        """
        -------------ZhangChengLiang Bank---------------
        \033[31;1m
        1.  账户信息
        2.  存款
        3.  取款
        4.  转账
        5.  账单
        6.  退出
        \033[0m"""
    )
    menu_dic = {
        "1":account_info,
        "2":repay,
        "3":withdraw,
        "4":transfer,
        "5":paycheck,
        "6":logout
    }
    flag = False
    while not flag:
        print(msg)
        choice = input("<<<:").strip()
        if choice in menu_dic:
            #很重要！！省了很多代码，不用像之前一个一个判断！
            menu_dic[choice](access_data)

        else:
            print("\033[31;1mYou choice doesn't exist!\033[0m")



def run():
    """
    当程序启动时调用，用于实现主要交互逻辑
    :return:
    """
    # 调用认证模块,返回用户文件json.load后的字典,传入access_logger日志对象
    access_data = auth.access_login(user_data, access_logger)
    print("AA")
    if user_data["is_authenticated"]:       #如果用户认证成功
        print("has authenticated")
        #将用户文件的字典赋给user_data["account_data"]
        user_data["account_data"] = access_data
        interactive(user_data)   #用户交互开始