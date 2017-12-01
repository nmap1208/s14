#Auther nmap

my_age = 28
print("Now let's play a game,you guess my age,you have 3 times")
for i in range(3):
  age=int(input("pls input a number:"))
  if age == my_age:
      print("yes.you got it")
      break
  elif age > my_age:
      print("you think bigger")
  else:
      print("you think small")
else:
  print("enough 3 times,fuck off")
