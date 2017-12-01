#Auther nmap
"""
交易模块，处理用户金额移动
"""
from conf import settings
from core import account
from core import log

def make_transaction(account_data,transcation_type,amount,log_obj,**kwargs):
    """
    处理用户的交易
    :param account_data:字典，用户的帐户信息
    :param transaction_type:用户交易类型，repay or withdraw...
    :param amount:交易金额
    :return:用户交易后帐户的信息
    """
    amount=float(amount)  #将字符串类型转换为float类型
    if transcation_type in settings.TRANSACTION_TYPE:
        interest=amount*settings.TRANSACTION_TYPE[transcation_type]["interest"]   #利息计算
        old_balace= account_data["balance"]  #用户原金额
        print(interest,old_balace)
        # 如果帐户金额变化方式是"plus"，加钱
        if settings.TRANSACTION_TYPE[transcation_type]["action"]=="plus":
            new_balance=old_balace+amount+interest
            log_obj.info("Your account repay%s,your account new balance is %s"%(amount,new_balance))
            # 如果帐户金额变化方式是"minus",减钱
        elif settings.TRANSACTION_TYPE[transcation_type]["action"]=="minus":
            new_balance=old_balace-amount-interest
            log_obj.info("Your account withdraw%s,your account new balance is %s" % (amount, new_balance))
            if new_balance<0:
                print("Your Credit [%s] is not enough for transaction [-%s], "
                      "and Now your current balance is [%s]" % (account_data["credit"], (amount+interest), old_balace))
                return
        account_data["balance"]=new_balance
        account.dump_account(account_data)    #调用core下account模块将已更改的用户信息更新到用户文件
        return account_data
    else:
        print("Transaction is not exist!")