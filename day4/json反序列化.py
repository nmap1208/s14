#Auther nmap
import pickle
def sayhi(name):
    print('hello2:',name)
f1=open('info.txt','rb')
data=pickle.loads(f1.read())
data=pickle.load(f1)
print(data)
print(type(data))
print(data['func']('nmap'))

