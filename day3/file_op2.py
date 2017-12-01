#Auther nmap
f=open('yesterday',encoding='utf-8',mode='r+')
#for index.html,line in enumerate(f):
#    if index.html==9:
#        continue
#    print(line)
#
count=0
for line in f:
    count+=1
    if count==10:
        continue
    print(line)