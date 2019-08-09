# -*- coding:utf-8 -*-

import requests


# 会话对象 跨请求保持某些参数, 同一个Session实例发出的所有请求之间保持cookie
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/name/value')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)
# 会话也可用来为请求方法提供缺省数据，通过会话属性来实现
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'t-test2': 'false'})
print(r.text)
