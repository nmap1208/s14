#Auther nmap
#认证模块
import os
import json
import time

from core import db_handle
from conf import settings

def access_auth(account,password,log_obj):
    """
    下面的access_login调用access_auth方法，用于登陆
    :param acount: 用户名
    :param password: 密码
    :return:如果未超期，返回字典，超期则打印相应提示
   """
    db_path=db_handle.handle(settings.DATABASE) #调用db_handle下的handle方法,返回路径/db/accounts
    print(db_path)
    account_file="%s/%s.json"%(db_path,account)  #用户文件
    print(account_file)
    if os.path.isfile(account_file):                 #如果用户文件存在(即用户存在)
        with open(account_file,"r",encoding="utf-8") as f:  #打开文件
            account_data = json.load(f)       #file_data为字典形式
            print(account_data)
            if account_data["password"]==password:
                expire_time=time.mktime(time.strptime(account_data["expire_date"],"%Y-%m-%d"))
                #print(expire_time)
                #print(time.strptime(account_data["expire_date"],"%Y-%m-%d"))
                if time.time()>expire_time:     #如果信用卡已超期
                    log_obj.error("Account [%s] had expired,Please contract the bank" % account)
                    print("Account %s had expired,Please contract the bank"%account)
                else:                         #信用卡未超期，返回用户数据的字典
                    #print("return")
                    log_obj.info("Account [%s] logging success" % account)
                    return account_data
            else:
                log_obj.error("Account or Passworddoes not correct!")
                print("Account or Passworddoes not correct!")
    else:#用户不存在
        log_obj.error("Account [%s] does not exist!" % account)
        print("Account [%s] does not exist!"%account)


def access_login(user_data,log_obj):
    """
    用记登陆，当登陆失败超过三次则退出
    :param user_data: main.py里面的字典
    :return:若用户帐号密码正确且信用卡未超期，返回用户数据的字典
    """
    retry=0
    while not user_data["is_authenticated"] and retry<3:
        account=input("Account:").strip()
        password= input("Password:").strip()   #用户帐号密码正确且信用卡未超期，返回用户数据的字典
        user_auth_data=access_auth(account,password,log_obj)
        if user_auth_data:
            user_data["is_authenticated"]=True   #用户认证为True
            user_data["account_id"]=account       #用户帐号ID为帐号名
            print("welcome %s"%account)
            return user_auth_data
        retry+=1
    else:
        print("Account [%s] try logging too many times..." % account)
        log_obj.error("Account [%s] try logging too many times..." % account)
        exit()