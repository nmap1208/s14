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
    for index,product_price in enumerate(Product_list):
        product=product_price[0]
        price=product_price[1]
        print(index+1,'.',product,'----',price)
    break