#Auther nmap
import random
checkcode=''
for i in range(4):
    current=random.randint(1,9)
    checkcode+=str(current)
print(checkcode)