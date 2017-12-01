#Auther nmap
import time
user='nmap'
passwd='abc123'
def auth(auth_type):
    def out_wrapper(func):
        def wrapper(*args,**kargs):
                if auth_type=='local':
                    print('auth local------------')
                    username=input('Username:').strip()
                    password=input('Password:').strip()
                    if user==username and passwd==password:
                        print('\033[32;1mUser has passed authentication\033[0m')
                        func(*args,**kargs)  #from home
                    else:
                        exit('\033[31;1mInvalid username or password\033[0m')
                elif auth_type=='ldap':
                    print('auth ldap-------------')
                    username=input('Username:').strip()
                    password=input('Password:').strip()
                    if user==username and passwd==password:
                        print('\033[32;1mUser has passed authentication\033[0m')
                        func(*args,**kargs)  #from home
                    else:
                        exit('\033[31;1mInvalid username or password\033[0m')
        return wrapper
    return out_wrapper

def index():
    print('welcome to index.html page')

@auth(auth_type='local')
def home():
    print('welcome to home page')

@auth(auth_type='ldap')
def bbs():
    print('welcome to bbs page')

index()
home()
bbs()
