#Auther nmap
#-*-coding:utf-8-*-
import os
print (os.path)
#cmd_res = os.system("dir")


os.makedirs("d3/222/333")
cmd_res = os.popen("dir").read()
print("--->",cmd_res)