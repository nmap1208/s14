#Auther nmap
#-*-encoding:utf-8-*-
sql_file=open('update_1','w',encoding='utf-8')
nickname=[
    '汉芬菲','连世英','言心','静逸','hehe','厚孤晴',
    '初蝶','夏青','沃德','轩辕','痴梅','9527','莫忆枫',
    '申屠','甄梦','燕舒怀','丹雪','雨墨','小青年','公子',
    '花未染','苏婉柔','轩小希','傲無情','公爵','99875','久念',
    '孤瘾','心如止水','迷醉','坏小孩','影','独行侠','平步青云',
    '夜场嗨青春','无敌小战神','音乐','气质','青春最珍贵','jack',
    '世界','王者','呐喊stop','滥情','潮男','亚洲太子','我心起扬',
    'sb','删除','寂寞','笑看','红尘','孤云','曲一凡','11111',
    '饶启','石羊','艾宁','嵇门','余强','全通','马泰','易','尉迟罕',
    '解东','萝国仙','蒲明','爱宇','巫元','亢巴','庆余年','长文','竹月',
    '文星','衣永元','笑天','亦云','长田秋子','吉崎美子','孔平','冀仪',
    '饶高','羊黎','南柳','伦高正','鲁广','钱旗','西门','沁经兰','倪山',
    '居田','禹国','安盖''英才','网络','水念文','功健','柏闵','恨风寒',
    '清韵','新瑶','明辉','揭小星','雨真','永丰','公','羊蕴和','欧欣',
    '基力辰','韦洪琳','芳衷','振荣苑','代珊','莫娟娟','alex','mentu',
    '彩虹','夜半呻吟','最懂的人','水煮今生','歌姬','萝莉','相见恨晚',
    '不会伪善','丢了温柔','隔壁老王','风与','白鹿'
]

num=0
c_numbercode=50001970
while num<len(nickname):
    line="update tab_user set c_nickname='%s'  where c_numbercode='%d';" %(nickname[num],c_numbercode)
    sql_file.write(line+'\n')
    num+=1
    c_numbercode+=1

















