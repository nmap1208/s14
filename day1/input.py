#Auther nmap

name = input("name:")
password = input("password:")
age = int(input("age:"))
salary = int(input("salary:"))

print("age type:",type(age))
print("str age",type( str(age) ))
info='''
-------------info of  %s -----------
Your name is: %s
Your password is: %s
Your age is:%d
Your salary is:%d
''' %(name,name,password,age,salary)
print(info)
