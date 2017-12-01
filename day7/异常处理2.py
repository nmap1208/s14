#Auther nmap
# while True:
#     num1 = input('num1:')
#     num2 = input('num2:')
#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#         result = num1 + num2
#     except Exception as e:
#         print ('出现异常，信息如下：')
#         print (e)
try:
    raise Exception('错误了.....')
except Exception as e:
    print(e)