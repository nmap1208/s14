
__author__ = 'Alex Li'

import sys
print(sys.getdefaultencoding())


msg = "我爱北京天安门"
msg_to_gbk=msg.encode('gbk')
msg_to_utf8=msg.encode('utf-8')
gbk_to_uni=msg_to_gbk.decode('gbk')
utf8_to_gb2312=msg_to_utf8.decode('utf-8').encode('gb2312')
print(msg_to_gbk)
print(msg_to_utf8)
print(gbk_to_uni)
print(utf8_to_gb2312)