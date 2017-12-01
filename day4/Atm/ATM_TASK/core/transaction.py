#Auther nmap
from conf import setting
from core import accounts
from core import log

def make_transaction(account_data,transaction_type,amount,log_obj,**kargs):
    amount=float(amount)
    if transaction_type in setting.TRANSACTION_TYPE:
        interest=amount*setting.TRANSACTION_TYPE[transaction_type]['interest']
        old_balance=account_data['balance']
        print(interest,old_balance)
        if setting.TRANSACTION_TYPE[transaction_type]['action']=='plus':
            new_balance=old_balance+amount+interest
            log_obj.info('Your account repay is %s,your account new balance is %s'%(amount,new_balance))
        elif setting.TRANSACTION_TYPE[transaction_type]['action']=='minus':
            new_balance=old_balance-amount-interest
            log_obj.info('Your account withdraw %s,your account new balance is %s'%(amount,new_balance))
            if new_balance<0:
                print('Your Credit %s is not enough for transaction %s and Now your current balance is %s '%(account_data['credit'],amount+interest,old_balance))
                return
        account_data['balance']=new_balance
        accounts.dump_account(account_data)
        return account_data
    else:
        print('Transaction is not exist')
