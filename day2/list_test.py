#Auther nmap
import sys,getpass
user_file = open('account.txt','r')
user_list = user_file.readlines()
locked_file=open('locked.txt','r+')
locked_list=locked_file.readlines()
username=input("Please input your username:")
try_counts=3
#password=input("Please input your password:")
for locked_user in locked_list:
    if username==locked_user:
        sys.exit('用户%s已经锁定' %username)
for user_line in user_list:
    (user,passwd) = user_line.strip().split()
    if username==user:
        while try_counts:
           password=input("Please input your password:")
           try_counts =try_counts-1
           if password==passwd:
               print("Welcome login %s" %username)
               sys.exit(0)
           else:
               print("password not right,please try again")
               print("You have only %s chances" %try_counts)
        if try_counts==0:
            print("You have tried 3 times,account locked")
            locked_file.write(username + '\n')
    else:          #因为每个账号都去匹配。n个账号，肯定会至少出现n-1个没匹配上的。
        pass
else:          #表示以上都循环遍历了，仍然没匹配上
    password=input("Please input your password:")  #这里仅仅模拟真实的网站登录，账号不存在的情况。不能说只输入账号就判断账号不存在吧
    print("user not exist,or password not right")
