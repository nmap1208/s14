#Auther nmap
import sys
Product_list=[  ['Iphone',500],['Car',1000],['coffee',30],['computer',800]  ]
Shopping_Cart=[]
salary=input("please input your salary:")
if salary.isdigit():
    salary=int(salary)
else:
    print('salary is not numberic')
    sys.exit(1)
while True:
    accout=salary
    print('products for sale:')
    for product_price in Product_list:
        product=product_price[0]
        price=product_price[1]
        i=Product_list.index(product_price)+1
        print(i,'.',product,'----',price)
    print(len(Product_list)+1,'.exit the program')
    if len(Shopping_Cart)==0:
        print('You have \033[31;1m%s\033[0m to use'%(accout))
    else:
        for p_b_price in Shopping_Cart:
                p_b=p_b_price[0]
                p_price=p_b_price[1]
                accout=accout-p_price
        print('You have \033[31;1m%s\033[0m to use'%(accout))
    choice_num=input('Please input a number to choice:')
    if choice_num.isdigit():
        choice_num=int(choice_num)
    else:
        print('Your input is not numberic,please try again:')
        continue
    if choice_num>0 and choice_num < len(Product_list)+1:
        ac=accout-Product_list[choice_num-1][1]
        if ac>=0:
            Shopping_Cart.append(Product_list[choice_num-1])
            print('Your got these products:')
            for p_b_price in Shopping_Cart:
                p_b=p_b_price[0]
                p_price=p_b_price[1]
                print( p_b)
            print('-----------------------------------')
        else:
            print('Your money is not enough,please choice again')
            continue
    elif choice_num==len(Product_list)+1:
        print('Your got these products:')
        print('###################################')
        for p_b_price in Shopping_Cart:
                p_b=p_b_price[0]
                p_price=p_b_price[1]
                print( p_b)
        print('###################################')
        print('The remaining money is %d  '%(accout))
        sys.exit(0)
    else:
        print('Your number is not correct')
        continue


