#Auther nmap
product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('book',120)
]
shopping_list = []
salary = input('Input your salary:')
if salary.isdigit():
    salary=int(salary)
    while True:
        for index,item in enumerate(product_list):
                print(index,item)
        user_choice=input("what do you want buy?>>>:")
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice<len(product_list) and user_choice>=0:
                p_item=product_list[user_choice]
                if p_item[1]<=salary:
                    shopping_list.append(p_item)
                    salary-=p_item[1]
                    print("add %s into shopping cart,your current balance is %d"%(p_item,salary))
                else:
                    print("your balance is %d ,it is not enough "%(salary))
            else:
                print("product code %s is not exist"%(user_choice))
        elif user_choice=='q':
            print('--------shopping list--------')
            for p in shopping_list:
                print(p)
            print('your current balance:',salary)
            exit()
        else:
            print('Invalid option')
