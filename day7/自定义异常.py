#Auther nmap
class WupeiqiException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise WupeiqiException('我的异常')
except WupeiqiException as e:
    print (e)