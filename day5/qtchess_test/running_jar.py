#Auther nmap
appList = {
	1:{"appName":"ddz_1.jar",'isLaunch':False,'pid':0, 'justOpen':'False'},
	2:{"appName":"ddz_2.jar",'isLaunch':False,'pid':0, 'justOpen':'False'},
	# and so on
}
# 新建一个文件索引列表.  第一层为所有的app, 下标数字1开始
# 每一个文件有 appName文件名字(做启动用)  isLaunch是否启动 pid进程号

for k,v in appList.items():
    print(appList[k]['appName'])
    appList[k]['isLaunch']='True'

	# app.pid = 启动程序方法(app.appName) #使用python提供的启动程序方法, 启动成功后如果会返回pid,那么就给pid赋值
	# app.isLaunch = True #启动成功后,isLaunch标记ture
print(appList)
# 启动之后, 间隔一段时间再执行接下来的操作, 保证所有app都加载完毕

# del MONITOR_TIME = 120 #设置一个定时器的监测时间
# def scheduleCheckApp()
# 	# 按照一定规则关闭程序
#
# 	for app in appList:
# 		if app.isLaunch == false:
# 			app.pid = 启动程序方法(app.appName)
# 			app.isLaunch = True
# 			app.justOpen = True #防止刚开启,就被关掉
#
#
# 	for app in appList:
# 		if app.isLaunch == True and app.justOpen == False:
# 			关闭程序(app.pid)
# 			app.isLaunch = False
#
# 	for app in appList:
# 		app.justOpen = False
#
#
# del timerCheckApp = threading.Timer(MONITOR_TIME, scheduleCheckApp)
# timerCheckApp.start()

