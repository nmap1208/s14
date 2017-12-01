#_*_ coding:utf-8 _*_
import os,getpass,sys
i = 0
while i < 3:
        name = input('请输入用户名:')
        lock_file = open('account_lock.txt','r+')
        lock_list = lock_file.readlines()
        for lock_line in lock_list:
                if name == lock_line:
                        sys.exit('用户%s已经锁定' %name)
        user_file = open('account.txt','r')
        uer_list = user_file.readlines()
        for user_line in user_file:
                [user,password] = user_line.split()
                if name == user:
                        j = 0
                        while j < 3:
                                passwd = getpass.getpass('请输入密码:')
                                if passwd == password:
                                        print ('登录成功%s'%name)
                                        sys.exit(0)
                                else:
                                        if j != 2:
                                                print('用户 %s 密码错误，请重新输入，还有 %d 次机会' % (name,2 - j))
                                j+=1
                        else:
                                lock_file.write(name + '\n')
                                sys.exit('用户 %s 达到最大登录次数，将被锁定并退出' % name)
                else:
                        pass
        else:
                if i !=2:
                        print('用户 %s 不存在，请重新输入，还有 %d 次机会' % (name,2 - i))
        i+=1
else:
        sys.exit('用户 %s 不存在，退出' % name)
lock_file.close()                                                   #关闭LOCK文件
user_file.close()