# encoding=utf8

import socket
import time

data = {u'移动1':'10086.cn',
        u'移动2':'shop.10086.cn',
        u'联通1':'mall.10010.com',
        u'联通2':'10010.com',
        u'联通3':'s.10010.com',
        u'联通4':'iservice.10010.com',
        u'电信1':'189.cn',
        u'电信2':'shouji.189.cn'
        }

result = {}
for k,v in data.items():
    ips = []
    ips1= []
    for i in range(100):
        # time.sleep(2)
        ip = socket.gethostbyname(v)
        ips.append(ip)
        ips1 = list(set(ips))
    result[v]=ips1

print result