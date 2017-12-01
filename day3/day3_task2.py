#Auther nma
# arg = {
#     'bakend': 'www.oldboy.org',
#     'record':{
#         'server': '100.1.7.9',
#         'weight': 20,
#         'maxconn': 30
#     }
# }
info='''
This is a tool to manage haproxy config file
1.delete a backend
2.update a backend
3.show all backend
4.add a backend
'''
list_backend=[]
print(info)
choice_num=input('please input correct number to do some thing:')
if choice_num.isdigit():
    choice_num=int(choice_num)
    if choice_num==3:
        data=open('task_file2','r',encoding='utf-8')
        list_data=data.readlines()
        len_data=len(list_data)
        for line in list_data:
            if line.strip().startswith('backend'):
                back_pos=list_data.index(line)
                break
        for line_new in list_data[back_pos:]:
            list_backend.append(line_new)
            print(line_new.strip())
        print(list_backend)
        b1=list_backend[0]
        print(b1)
        b2=list(b1.split())
        print(b2)

    elif choice_num==1:
        choice_del=input('please input a backend server you want to delete:')
        choice_dict=eval(choice_del)
        choice_dict=eval(choice_dict)
        print(choice_dict)
        print(type(choice_dict))
        for (k,v) in choice_dict.items():
            print(k,v)
















