#Auther nmap

# import hashlib
#
# m = hashlib.md5()
# m.update(b"Hello")
# print(m.hexdigest())
# m.update(b"It's me")
# print(m.hexdigest())
#
# m2=hashlib.md5()
# m2.update(b"HelloIt's me")
# print(m2.hexdigest())
import hmac
h = hmac.new(b'abckey', '宝塔镇河妖'.encode(encoding='utf-8'))
print (h.hexdigest())
print (hmac.new(b"mykey","Hello world !".encode(encoding='utf-8')).hexdigest())


h=hmac.new(b'hehe')
h.update('测试'.encode(encoding='utf-8'))
print(h.hexdigest())

print (hmac.new(b"hehe",'测试'.encode(encoding='utf-8')).hexdigest())