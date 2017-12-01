#Auther nmap

my_age = 28
print("Now let's play a game,you guess my age,you have 3 times")
count = 3
while count:
  age=int(input("pls input a number:"))
  count = count-1
  if age == my_age:
      print("yes.you got it")
      break
  elif age > my_age:
      print("you think bigger")
      print("you have only {chance} ".format(chance=count))
  else:
      print("you think small")
      print("you have only {chance} ".format(chance=count))
else:
  print("enough 3 times,fuck off")