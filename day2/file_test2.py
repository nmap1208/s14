#Auther nmap
#three files
# product_list.txt--store products
# shopping_cart.txt--store products has been bought
# money.txt --store money
import sys
import copy
p1=open('product_list.txt','r')    #p1存储商品列表，买家只读方式打开
s1=[]
x1=p1.readlines()
for i in x1:
    i=i.strip()
    i=eval(i)
    s1.append(i)
p1.close()  #读取完毕关闭文件
print(s1)

p2=open('shopping_cart.txt','r+')    #p2存储买家购买的商品，可以可以读写打开。
s2=[]
x2=p2.readlines()
for i in x2:
    i=i.strip()
    i=eval(i)
    s2.append(i)
p2.close()
print(s2)

p3=open('money.txt','r+')    #p3存储用于余额。可以通过长度大小判断是否第一次登录
s3=p3.readline()   #这里使用readline，获取的是字符串，这样才能使用int转换，如果使用readlines的话获取的是列表。无法用int转换
p3.close()
if len(s3)==0:
    salary = int(input('Input your salary:'))
    while True:
        for product_price in s1:
            product=product_price[0]
            price=product_price[1]
            i=s1.index(product_price)+1
            print(i,'.',product,'----',price)
        user_choice=input('what do you want buy?,enter "q" if you want quit>>>:')
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice>=1 and user_choice<=len(s1):
                p_item=s1[user_choice-1]
                if p_item[1]<=salary:
                    s2.append(p_item)
                    salary-=p_item[1]
                    print("add %s into shopping cart,your current balance is %d"%(p_item[0],salary))
                else:
                    print("your balance is %d ,it is not enough "%(salary))
            else:
                print("product code %s is not exist"%(user_choice))
        elif user_choice=='q':
            print('--------shopping list--------')
            for p in s2:
                print(p)
            f2=open('shopping_cart.txt','w')
            for i in s2:        #保存配置到文件中
                 if s2.index(i)==len(s2)-1:
                     i=str(i)
                     f2.write(i)
                 else:
                     i=str(i)
                     f2.write(i)
                     f2.write('\n')
            f2.flush()
            f2.close()
            print('shopping data has been saved')
            print('your current balance:',salary)
            f3=open('money.txt','w')
            salary=str(salary)
            f3.write(salary)
            f3.flush()
            f3.close()
            print('your balance has been saved')
            exit()
        else:
            print('Invalid option')
else:
    salary=int(s3)
    while True:
        for product_price in s1:
            product=product_price[0]
            price=product_price[1]
            i=s1.index(product_price)+1
            print(i,'.',product,'----',price)
        user_choice=input('what do you want buy?,enter "q" if you want quit>>>:')
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice>=1 and user_choice<=len(s1):
                p_item=s1[user_choice-1]
                if p_item[1]<=salary:
                    s2.append(p_item)
                    salary-=p_item[1]
                    print("add %s into shopping cart,your current balance is %d"%(p_item[0],salary))
                else:
                    print("your balance is %d ,it is not enough "%(salary))
            else:
                print("product code %s is not exist"%(user_choice))
        elif user_choice=='q':
            print('--------shopping list--------')
            for p in s2:
                print(p)
            f2=open('shopping_cart.txt','w')
            for i in s2:        #保存配置到文件中
                 if s2.index(i)==len(s2)-1:
                     i=str(i)
                     f2.write(i)
                 else:
                     i=str(i)
                     f2.write(i)
                     f2.write('\n')
            f2.flush()
            f2.close()
            print('shopping data has been saved')
            print('your current balance:',salary)
            f3=open('money.txt','w')
            salary=str(salary)
            f3.write(salary)
            f3.flush()
            f3.close()
            print('your balance has been saved')
            exit()
        else:
            print('Invalid option')