#Auther nmap
import sys
info={
    '浙江':{
        '杭州':
          ['西湖区','上城区','下城区','江干区']
        ,
        '温州':['鹿城区','瓯海区','龙湾区'
        ],
        '湖州':['吴兴区','南浔区','德清县','长兴县','安吉县']
    },

    '江苏':{
        '南京':['玄武区', '白下区', '秦淮区', '建邺区'],
        '徐州':['泉山区', '云龙区', '鼓楼区', '九里区']
    },

    '安徽':{
        '合肥':['蜀山区','瑶海区','庐阳区','包河区'],
        '宿州':['萧县','砀山县','灵璧县','泗县','埇桥区']
    }
}

print('province ---------:')
while True:
    for province in info:
        print(province)
    print('enter "q" if you want quit====>:')
    p1=input('please have a choice to select a province=====>:')
    if p1=='q':
        sys.exit(0)
    else:
        ret1=p1 in info
        while ret1:
            for city in info[p1]:
                print(city)
            print('enter "q" if you want quit====>:')
            print('enter "b" if you want go back:')
            p2=input('have a choice  city or quit or back:')
            if p2=='q':
                sys.exit(0)
            elif p2=='b':
                break
            else:
                ret2= p2 in info[p1]
                while ret2:
                    for area in info[p1][p2]:
                        print(area)
                    print('enter "q" if you want quit:')
                    print('enter "b" if you want go back:')
                    p3=input('your choice:')
                    if p3=='q':
                        sys.exit(0)
                    elif p3 =='b':
                        break
                    else:
                        print('it is not correct answer,try again:')
                print('city not exist ,please input a correct string:')
        else:
            print('province not exist ,please input a correct string:')


























