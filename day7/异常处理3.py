#Auther nmap
class NmapException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise NmapException('我的异常')
except NmapException as e:
    print (e)