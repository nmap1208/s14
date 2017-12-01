#Auther nmap
import re
# print(re.split('[1-9]+','abc324ddf000uuupp8834yyyff91kk'))
# print(re.split('[1-9]','abc324ddf000uuupp8834yyyff91kk'))
# print(re.sub('[0-9]','|','886jjffkk9966fffddd90cc'))
# print(re.sub('[0-9]+','|','886jjffkk9966fffddd90cc'))
#calc='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
calc2='1-((-1 +33*2-22 )-(33-2))'   #匹配括号
#calc2='(222)'
calc2_new=re.sub('\s','',calc2)
print('calc2_new:',calc2_new)
print(re.search('\(-?(\d)+(\d|\.|\+|\-|\*|\/)*(\+|\-|\*|\/)(\d|\.|\+|\-|\*|\/)*(\d)+\)',calc2_new))
catch=re.search('\(-?(\d)+(\d|\.|\+|\-|\*|\/)*(\+|\-|\*|\/)(\d|\.|\+|\-|\*|\/)*(\d)+\)',calc2_new)
if catch !=None:
    print(catch.group())
    catch_it=catch.group()
    catch_it=re.sub('\(|\)','',catch_it)
    print(catch_it)
else:
        print('None')



#print(re.sub('--','+','1--2--3'))  匹配两个减号
# data1='(2.22)'        #匹配括号内的纯数字
# data_1=re.search('\((\s|-)?(\d|\.|\d|\s)+\s*\)',data1)
# print(data_1)
# data2='(-2.22)'
# data_2=re.search('\((\s|-)?(\d|\.|\d|\s)+\s*\)',data2)
# print(data_2)
# data3='(-2)'
# data_3=re.search('\((\s|-)?(\d|\.|\d|\s)+\s*\)',data3)
# print(data_3)
# data4='(256)'
# data_4=re.search('\((\s|-)?(\d|\.|\d|\s)+\s*\)',data4)
# print(data_4)
# data5='(256-2)'
# data_5=re.search('\((\s|-)?(\d|\.|\d|\s)+\s*\)',data5)
# print(data_5)
# data6='(- 22)'
# data_6=re.search('\((\s|-)?(\d|\.|\d|\s)+\s*\)',data6)
# print(data_6)
# data7='( - 22)'
# data7=re.sub('\s','',data7)
# data_7=re.search('\((\s|-)?(\d|\.|\d|\s)+\s*\)',data7)
# print(data_7)

# calc='1 - 2 * (   (60-30 +(-40/5) *   (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# calc_new=re.sub('\s','',calc)
# print(calc_new)