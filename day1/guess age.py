#Auther nmap


my_age=int('28')
print("Now let's play a game,you guess my age")
age=int(input("pls input a number:"))

if age==my_age:
    print("yes.you got it")
elif age > my_age:
    print("you think bigger")
else:
    print("you think small")
