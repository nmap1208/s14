#Auther nmap
import sys
import copy
p1=open('product_list.txt','r+')
s1=[]
x1=p1.readlines()
for i in x1:
    i=i.strip()
    i=eval(i)
    s1.append(i)
p1.close()  #读取完毕关闭文件
print(s1)
print('products for sale:')
#for product_price in s1:
#    product=product_price[0]
#    price=product_price[1]
#    i=s1.index.html(product_price)+1
#    print(i,'.',product,'----',price)
while True:
    for product_price in s1:
        product=product_price[0]
        price=product_price[1]
        i=s1.index(product_price)+1
        print(i,'.',product,'----',price)
    choice1=input('enter "q"  exit the program , "m"--modify ,"a"--add ,"d"--del  ==>: ')
    if choice1=='q':
        sys.exit(0)
    elif choice1=='m':
#        for product_price in s1:
#            product=product_price[0]
#            price=product_price[1]
#            i=s1.index.html(product_price)+1
#            print(i,'.',product,'----',price)
        while True:
            for product_price in s1:
                product=product_price[0]
                price=product_price[1]
                i=s1.index(product_price)+1
                print(i,'.',product,'----',price)
            choice_m=input('enter a number to select a product===>')
            if choice_m.isdigit():    #通过数字选择项要改的商品，先判断是否是数字
                choice_m=int(choice_m)
                if choice_m>=1 and choice_m<=len(s1):  #数字在有效范围内
                    print('you want to modify this===>\n',s1[choice_m-1][0],s1[choice_m-1][1]) #你想改它
                    while True:
                        choice_m_1=input('enter "0" -- modify name,"1"  modify price,"2" --back to upper list ===>:') #改名还是改价,2返回上一级
                        if choice_m_1.isdigit():    #先判断是否是数字
                            choice_m_1=int(choice_m_1)
                            if choice_m_1==0:    #是数字0改商品名字
                                prod_name_ori=s1[choice_m-1][0]
                                prod_name=input('enter a new name replace %s' %(s1[choice_m-1][0]))
                                s1[choice_m-1][0]=prod_name
                                print('modify success---#############')
                                print(s1)
                                while True:
                                    save_or_not=input('enter "s" to save the modified name,"c" if you want cancel')
                                    if save_or_not=='s':   #保存配置
                                        f1=open('product_list.txt','w')
                                        for i in s1:        #保存配置到文件中
                                            if s1.index(i)==len(s1)-1:
                                                i=str(i)
                                                f1.write(i)
                                            else:
                                                i=str(i)
                                                f1.write(i)
                                                f1.write('\n')
                                        f1.flush()
                                        f1.close()
                                        print('data has saved')
                                        sys.exit(0)
                                    elif save_or_not=='c':
                                        s1[choice_m-1][0]=prod_name_ori
                                        print('you have cancel the modify')
                                        print(s1)
                                        break
                                    else:
                                        print('Invalid answer,enter s or c')
                                        continue
                            elif choice_m_1==1: #数字1改价格
                                while True:
                                    price_new=input('enter a new price replace %s ===>' %(s1[choice_m-1][0]))
                                    if price_new.isdigit():
                                        price_ori=s1[choice_m-1][1]
                                        price_new=int(price_new)
                                        s1[choice_m-1][1]=price_new
                                        print('modify price success---###########')
                                        print(s1)
                                        while True:
                                            save_or_not=input('enter "s" to save the modified price,"c" if you want cancel')
                                            if save_or_not=='s':   #保存配置
                                                f1=open('product_list.txt','w')
                                                for i in s1:        #保存配置到文件中
                                                    if s1.index(i)==len(s1)-1:
                                                        i=str(i)
                                                        f1.write(i)
                                                    else:
                                                        i=str(i)
                                                        f1.write(i)
                                                        f1.write('\n')
                                                f1.flush()
                                                f1.close()
                                                print('data has saved')
                                                sys.exit(0)
                                            elif save_or_not=='c':
                                                s1[choice_m-1][1]=price_ori
                                                print('you have cancel the modify')
                                                print(s1)
                                                break
                                            else:
                                                print('Invalid answer,enter s or c')
                                                continue
                                    else:
                                        print('Invalid type of price,please enter a number')
                            elif choice_m_1==2:
                                break
                            else:    #其余数字提示无效
                                print('not Invalid number ,enter 0 or 1 or 2')
                        else:  #不是数字
                            print('price or name --your input is not a number')
                else:  #数字不在有效范围内
                    print('product choice --Invalid number ,try again')
            else:     #如果说输入的不是数字。提示请重试。从循环同步开始重新输入
                print('it is not a number,please try again')
    elif choice1=='a':
        while True:
            choice_a_name=input('enter the product name you want add===>:')
            choice_a_price=input('enter the product price you want ===>:')
            if choice_a_price.isdigit():
                choice_a_price=int(choice_a_price)
                s1_ori=copy.deepcopy(s1)  #这里之所以使用深拷贝，不用引用，是因为你添加1个之后。s1就变化了。s1_ori引用也变了，下面的c取消没作用
                s1.append([choice_a_name,choice_a_price])
                print('add successful')
                print(s1)
                exit_flag=1
                while exit_flag:
                    save_or_not=input('enter "s"----save ,"c"------cancel')
                    if save_or_not=='s':   #保存配置
                        f1=open('product_list.txt','w')
                        for i in s1:        #保存配置到文件中
                            if s1.index(i)==len(s1)-1:
                                i=str(i)
                                f1.write(i)
                            else:
                                i=str(i)
                                f1.write(i)
                                f1.write('\n')
                        f1.flush()
                        f1.close()
                        print('data has saved')
                        sys.exit(0)
                    elif save_or_not=='c':
                        print('you have cancel the add')
                        s1=s1_ori
                        print(s1)
                        while exit_flag:
                            choice_a_c=input('enter "q" if you want quit the program,"n"--contine add===>:')
                            if choice_a_c=='q':
                                sys.exit(0)
                            elif choice_a_c=='n':
                                exit_flag=0
                                break
                            else:
                                print('enter "q" or "n"')
                    else:
                        print('Invalid answer,enter s or c')
                        continue
            else:
                print('please input numberic for the product price')
    elif choice1=='d':
        for product_price in s1:
            product=product_price[0]
            price=product_price[1]
            i=s1.index(product_price)+1
            print(i,'.',product,'----',price)
        while True:
            choice_d=input('enter the number you want delete,enter "q" if you quit the program===>:')
            if choice_d.isdigit():    #通过数字选择项要改的商品，先判断是否是数字
                s1_ori=copy.deepcopy(s1)
                choice_d=int(choice_d)
                if choice_d>=1 and choice_d<=len(s1):  #数字在有效范围内
                    del s1[choice_d-1] #你想改它
                    print('delete successful')
                    print(s1)
                    while True:
                        save_or_not=input('enter "s"----save ,"c"------cancel')
                        if save_or_not=='s':   #保存配置
                            f1=open('product_list.txt','w')
                            for i in s1:        #保存配置到文件中
                                if s1.index(i)==len(s1)-1:
                                    i=str(i)
                                    f1.write(i)
                                else:
                                    i=str(i)
                                    f1.write(i)
                                    f1.write('\n')
                            f1.flush()
                            f1.close()
                            print('data has saved')
                            sys.exit(0)
                        elif save_or_not=='c':
                            print('you have cancel the del')
                            s1=s1_ori
                            print(s1)
                            break
                        else:
                            print('Invalid answer,enter s or c')
                            continue
                else:
                    print('please enter a number in between 1-%s' %(len(s1)))
            elif choice_d=='q':
                break
            else:
                print('please enter a number in between 1-%s,or enter "q" to exit the program===>:' %(len(s1)))
    else:
        print('not a correct answer---')