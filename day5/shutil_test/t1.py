#Auther nmap
#_*_encoding:utf-8_*_

import shutil,sys
# print(sys.getdefaultencoding())
# f1=open('a.txt',encoding='utf-8')
# f2=open('b.txt','w',encoding='utf-8')
# shutil.copyfileobj(f1,f2)
# shutil.copyfile('a.txt','c.txt')
# shutil.copystat('a.txt','d.txt')
# shutil.copytree('dir-1','dir-2')
# shutil.rmtree('dir-2')
# shutil.make_archive('dir2','gztar',root_dir='dir-1')
import zipfile
z=zipfile.ZipFile('dir.zip','w')
z.write('a.txt')
print('hehe')
z.write('b.txt')
print('--------')
z.write('dir-1')
z.close()
