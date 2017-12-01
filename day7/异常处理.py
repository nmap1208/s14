#Auther nmap
data={'name':'nmap','age':'22'}
names=['a','b']
try:
    print('hehe')
    names[3]
    #data['sex']
    #open('test.txt')
except (KeyError,IndexError) as e:
    print('没有这个key',e)
except IndexError as e:
    print('列表操作错误',e)
except Exception as e:
    print('出错了',e)

else:
    print('一切正常')
finally:
    print('不管有没有错，都执行')