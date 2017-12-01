#Auther nmap
import os,json

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(dir)
file="%s\ATM\db\\accounts\zcl.json"%dir
print(file)
with open(file, "r", encoding="utf-8") as f:
    account_data = json.load(f)
    print(account_data)



product_list =[
    ("Apple Iphone",6000),
    ("Apple Watch",4600),
    ("Books",600),
    ("Bike",750),
    ("cups",120),
    ("Apple",50),
    ("banana",60),
]
shopping_list =[]
salary = account_data["balance"]

while True:
    for index,item in enumerate(product_list):
        print (index,item)
    user_choice = input ("Enter the serial number:")
    if user_choice.isdigit():
        user_choice = int (user_choice)
        if user_choice <len (product_list) and user_choice >=0:
            p_item = product_list[user_choice]
            if p_item[1] <= salary:
                shopping_list.append(p_item)
                salary -= p_item[1]
                with open(file,"w+",encoding="utf-8") as f:
                    account_data["balance"]=salary
                    print(account_data)
                    json.dump(account_data,f)
                print ("Added %s into your shopping cart,your current balance is %s"%(p_item,salary))
            else:
                print ("Your balance is not enough！！")
        else:
            print ("The goods you entered do not exist")

    elif user_choice == "q":
        print ("====shopping list====")
        for p in shopping_list:
            print (p)
        print ("Your current balance is %s"%salary)
        exit()
    else:
        print ("invalid option")