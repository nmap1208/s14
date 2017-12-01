#Auther nmap
name = input("name:")
password = input("password:")
age = int(input("age:"))
salary = int(input("salary:"))

info='''
-------------info of  {0} -----------
Your name is: {0}
Your password is: {1}
Your age is:{2}
Your salary is:{3}
'''.format(name,password,age,salary)

print(info)