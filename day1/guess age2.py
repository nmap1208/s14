#Auther nmap

count = 3
my_age = 28
print("Now let's play a game,you guess my age,you have 3 times")
while count:
  age=int(input("pls input a number:"))
  if age == my_age:
      print("yes.you got it")
      break
  elif age > my_age:
      print("you think bigger")
  else:
      print("you think small")
  count -=1
  if count==0:
      choice=str(input("if you want play again ,input Y/N"))
      if choice=='Y':
         count=3
         continue
      elif choice=='N':
        break
      else:
          print("Invalid choice ")
          break
else:
  print("enough 3 times,fuck off")
