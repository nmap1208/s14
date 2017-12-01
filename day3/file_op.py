#Auther nmap
#f1=open('yesterday','r',encoding='utf-8')
#f2=open('yesterday2','w+',encoding='utf-8')
#for i in f1:
#        f2.write(i.replace('滋味是甜的','滋味是苦的',1))
#f1.close()
#f2.close()
with open('yesterday','r',encoding='utf-8') as f1  ,\
        open('yesterday2','r',encoding='utf-8') as f2:
    for line in f1:
        print(line.strip())
    print('############################################')
    for line2 in f2:
        print(line2.strip())

