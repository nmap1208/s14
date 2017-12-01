#Auther nmap
user_file = open('account.txt','r')
uer_list = user_file.readlines()
for user_line in user_file:
    user_line=user_line.split()
    (user,pw)=user_line
    print(user)