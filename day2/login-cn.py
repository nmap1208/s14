#Auther nmap
#Auther nmap
import sys,getpass
user_file = open('account.txt','r')
user_list = user_file.readlines()
locked_file=open('locked.txt','r+')
locked_list=locked_file.readlines()
username=input("请输入用户名:")
try_counts=3
for locked_user in locked_list:
    if username==locked_user:
        sys.exit('用户%s已经锁定' %username)
for user_line in user_list:
    (user,passwd) = user_line.strip().split()
    if username==user:
        while try_counts:
           password=input("请输入密码:")
           try_counts =try_counts-1
           if password==passwd:
               print("欢迎登录 %s" %username)
               sys.exit(0)
           else:
               print("密码不对")
               print("你还有%s次机会" %try_counts)
        if try_counts==0:
            locked_file.write(username + '\n')
            sys.exit("你已经用了3次机会，账号被锁定了")
    else:          #因为每个账号都去匹配。n个账号，肯定会至少出现n-1个没匹配上的。
        pass
else:          #表示以上都循环遍历了，仍然没匹配上
    password=input("请输入密码:")#这里仅仅模拟真实的网站登录，账号不存在的情况。不能说只输入账号就判断账号不存在吧
    print("账号不存在或者密码错误")