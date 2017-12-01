#Auther nmap
_username="nmap"
_passwd="abc123"

username=input("Your username:")
passwd=input("Your passwd:")

if _username == username and _passwd == passwd:
    print("Welcome user {name} login".format(name=_username))
else:
    print("Invalid username or password")