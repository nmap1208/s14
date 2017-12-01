#Auther nmap
import pickle

def sayhi(name):
    print('hello:',name)

info={
    'name':'nmap',
    'sex':'male',
    'age':22,
    'func':sayhi

}

f1=open('info.txt','wb')
f1.write(pickle.dumps(info))
pickle.dump(info,f1)
f1.close()