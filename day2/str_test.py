#Auther nmap
#name='nmap'
#print(name.capitalize())  #首字母大写
#print(name.upper())       #全部字母大写
#print(name.count('a'))    #统计个数
#say = 'my name is nmap'
#print(say.count('a'))
#print(name.center(50,'-'))   #center方法，把字符串放在中间。两边用多少个自定义的字符
#print(name.center(30,'#'))
#print(name.encode())   #把字符串转换成ascii码
#n2='李四'
#print(n2.encode())   #把字符串转换成ascii码
#print(name.endswith('ap'))  #末尾是否匹配的上字符串
#print(name.endswith('pa'))  #末尾是否匹配的上字符串
#name2='my name \tis nmap'
#print(name2.expandtabs(30)) #把tab键变成30个，没太大用处
#print(name2.find('a'))   #查找字符或者字符串位置，字符串也可以切片
#print(name2.find('me'))   #查找字符或者字符串位置，字符串也可以切片
#print(name2[name2.find('name'):9])  #字符串也可以切片
#print(name2[name2.find('name'):12])  #字符串也可以切片
#print(name2[name2.find('name'):])  #字符串也可以切片
#name3='my name is {name} ,i am {year} old'
#print(name3.format(name='nmap',year=23))   #format可以格式化数据
#print(name3.format_map({'name':'nmap','year':23}))  #format_map 可以结合字典格式化数据
#print(name3.index.html('name'))  #寻找下标，找到即返回位置
#print(name3.isalnum())   #是是否包含阿拉伯数字,同时不含有特殊字符
#print('abc123'.isalnum())  #是否包含阿拉伯数字,同时不含有特殊字符
#print('123'.isalnum())   #是否包含阿拉伯数字,同时不含有特殊字符
#print('123、'.isalnum())   #是否包含阿拉伯数字,同时不含有特殊字符
#print('123$'.isalnum())   #是否包含阿拉伯数字,同时不含有特殊字符
#print('abc'.isalpha())   #纯英文字符
#print('abc123'.isalpha())   #纯英文字符
#print('0x34'.isdecimal())   #方法检查字符串是否只包含十进制字符
#print('123'.isdecimal())   #方法检查字符串是否只包含十进制字符
#print('1230#'.isdecimal())   #方法检查字符串是否只包含十进制字符
#print('aa'.isdigit())
#p#rint('123'.isdigit())
#print('123.1'.isdigit())
#print('-123'.isdigit())
#print('a'.isidentifier())
#print('3a'.isidentifier())
#print('中国'.isidentifier())
#print('中国123ABC'.lower()) #把全部字母字符转换成小写
#print('中国123'.lower()) #把全部字母字符转换成小写,不会报错，返回原字符串
#print('33'.isnumeric())  #判断字符串是否只包含数字字符
#print('33.33'.isnumeric()) #判断字符串是否只包含数字字符
#print('中国'.isnumeric()) #判断字符串是否只包含数字字符
#print('中国33'.isnumeric()) #判断字符串是否只包含数字字符
#print('aa'.isnumeric()) #判断字符串是否只包含数字字符
#print(''.isspace())  #判断字符串是否仅包含空格或制表符。注意：空格字符与空白是不同的
#print(' '.isspace())  #判断字符串是否仅包含空格或制表符。注意：空格字符与空白是不同的
#print('a'.isspace())  #判断字符串是否仅包含空格或制表符。注意：空格字符与空白是不同的
#print('cd ef'.title())   #字符串中每个单词的首字母大写，其余小写
#print('3a rf'.title())  #字符串中每个单词的首字母大写，其余小写
#print('符串er fg'.title())  #字符串中每个单词的首字母大写，其余小写
#print('Ed Gf'.istitle())   #判断字符串每个单词的首字母是否大写。
#print('3A Rf'.istitle())   #判断字符串每个单词的首字母是否大写。
#print('符串Er fg'.istitle())   #判断字符串每个单词的首字母是否大写。
#print('3a'.isprintable())  #判断字符串所包含的字符是否全部可打印。字符串包含不可打印字符，如转义字符，将返回False。
#print('3a\t'.isprintable()) #判断字符串所包含的字符是否全部可打印。字符串包含不可打印字符，如转义字符，将返回False。
#print(''.join(['a','b','c','_','f']))
#print('abc'.join(['1','2','3','4','5']))
#print('45 07 89'.join(['1','2','3','4','5']))
#print('abc'.ljust(30,'#'))
#print('cc123'.ljust(32,'8'))
#print('abc'.rjust(30,'#'))
#print('cc123'.rjust(32,'8'))
#print('\tabc'.lstrip())
#print('\tabc'.rstrip())#
#print('\nabc'.lstrip())
#print('\nabc'.rstrip())
#print(' zzyyxxabc'.lstrip('zyx '))
#table = str.maketrans('cs', 'kz')
#print("please don't knock at my door!".translate(table))
#table = str.maketrans('cs', 'k#z', 'o')
#print("please don't knock at my door!".translate(table))
#print('AAABBBCCC'.replace('A','F'))
#print('AAABBBCCC'.replace('A','F',2))
#print(' abcbdbee '.split('b'))
#print(' abcbdbee '.split('bc'))
#Line = "AB\n" \
#       " CD\n" \
#       " EF"
#print(Line.splitlines())
#print(Line.splitlines(True))
#Line='AB, CD, EF'
#print(Line.splitlines())
#Line='AB CD EF'#
#print(Line.splitlines())
#print('dfcd'.startswith('df'))
#print('dfcd'.startswith('f'))
print('123'.zfill(5))
print('123'.zfill(6))




