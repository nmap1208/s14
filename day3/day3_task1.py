#Auther nmap

import sys,os
file=sys.argv[1]
find_str=sys.argv[2]
replace_str=sys.argv[3]

f=open(file,'r',encoding='utf-8')
f_new=open('file.bak','w',encoding='utf-8')

for line in f:
    f_new.write(line.replace(find_str,replace_str))
f.close()
f_new.close()

os.remove(file)
os.rename('file.bak',file)
#

# def sed(file,find_str,replace_str):
#     import sys,os
#     f=open(file,'r', encoding='utf-8')
#     f_new=open('file_new','w',encoding='utf-8')
#     for line in f
#         f_new.write(line.replace(find_str,replace_str))
#     f.close()
#     f_new.close()
#     os.remove(file)
#     os.rename('file_new',file)
#
# sed('yesterday','fly','flame')
