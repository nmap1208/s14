#Auther nmap
name = input("name:")
password = input("password:")
age = int(input("age:"))
salary = int(input("salary:"))


info='''
-------------info of  {_name} -----------
Your name is: {_name}
Your password is: {_password}
Your age is:{_age}
Your salary is:{_salary}
'''.format(
    _name=name,
    _password=password,
    _age=age,
    _salary=salary
)
print(info)