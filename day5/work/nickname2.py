#Auther nmap
#-*-encoding:utf-8:-*-
sql_file=open('update_2','w',encoding='utf-8')
nickname=['忆往昔','时间','淡化过去','没有人','全世界','温柔','暮涛','夕澜','金风','00000','矿泉水','不屑一顾','故人','忧郁的萨克''荒身心','往事随风','倾听','左手','真情','书成','画未','寂寞','无处安放','L','yyuuu','玉露','浮生','叶觞','墨离','红颜笑','我只为你Man','风伤','一直很低调','兮颜','暖风','寂寞的烟','苍白','的美','时光流逝','男人','走四方','北执','沧桑','喝酒','故城','三千歌','流怒','虚幻','思念','木兮','透骨''记忆','无力说爱','南笙','卡尺','须的狠','寒霜','冷露','剑胆','琴心','心如止水','看破红尘','苍天哥','笑醉','遥忘而立','君兮','朱砂','墨离','历史','朽','花殇','我','青橙','昔年','玲珑','青城','楚荆','湘竹','nan','9777f','古城老巷','乳此胸险','偷心贩子','傻友','不期而遇','慢热','慢热','烫心','多情','孤街浪徒','守侯','mmmm']
i=0
num=0
c_numbercode=50001000
while num<len(nickname):
    line="update tab_user set c_nickname='%s'  where c_numbercode='%d';" %(nickname[num],c_numbercode)
    sql_file.write(line+'\n')
    num+=1
    c_numbercode+=1