#Auther nmap
checkcode=''
import random
for i in range(4):
    current=random.randint(0,4)
    if current==i:
        tmp=chr(random.randint(65,90))
    else:
        tmp=str(random.randint(0,9))
    checkcode+=tmp
print(checkcode)
