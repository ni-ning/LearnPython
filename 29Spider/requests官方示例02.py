# -*- coding:utf-8 -*-

import requests

# 会话对象 跨请求保持某些参数, 同一个Session实例发出的所有请求之间保持cookie
# s = requests.Session()
# print(dict(s.cookies))  # {}
# r = s.get('http://httpbin.org/cookies/set/name/value')
# print(dict(r.cookies))  # {}
# print(dict(s.cookies))  # {'name': 'value'}
# r = s.get('http://httpbin.org/cookies')

# 会话也可用来为请求方法提供缺省数据，通过会话属性来实现
# s = requests.Session()
# s.auth = ('user', 'pass')
# s.headers.update({'x-test': 'true'})
# r = s.get('http://httpbin.org/headers', headers={'t-test2': 'false'})
# print(r.text)


# 请求与响应对象
'''
任何时候进行了类似 requests.get() 的调用，你都在做两件主要的事情:
其一，你在构建一个 Request 对象， 该对象将被发送到某个服务器请求或查询一些资源;
其二，一旦 requests 得到一个从服务器返回的响应就会产生一个 Response 对象, 
     该响应对象包含服务器返回的所有信息，也包含你原来创建的 Request 对象'''
# r = requests.get('http://en.wikipedia.org/wiki/Monty_Python', timeout=30)
# print(r.headers)
# print(r.request.headers)

'''
r.request其实使用了PreparedRequest，有时在发送请求之前，需要对body或header做一些额外的处理
要获取一个带有状态的 PreparedRequest，请用 Session.prepare_request() 取代 Request.prepare() 的调用
'''


# SSL 证书验证
# requests.get('https://requestb.in')     # SSL验证默认开启，如果证书验证失败，抛出SSLError
# https://requestb.in 没有设置SSL，所以失败

r = requests.get('https://github.com', verify=True)
print(r)


# SSL 证书验证
# https://baike.baidu.com/item/SSL证书/5201468
#
# verify
# 客户端证书
# cert
# CA 证书
#
#
# 响应体内容工作流
#
# stream=True -> Requests 无法将连接释放回连接池，除非你消耗了所有的数据，或者调用了Response.close
#
# 连接保持打开状态
# r.content -> 获取内容，
# 甚至通过r.iter_content和r.iter_lines方法来控制工作流
# 有或者r.raw从底层urllib3的HTTPResponse读取未解码的响应体
#
#
# requests支持流式上传，这允许你发送大的数据流或文件而无需先把它们读入内存
# 类文件对象
# with open('massive-body', 'rb') as f:
#     requests.post('http://some.url/streamed', data=f)
#
# 块编码请求
# POST对个分块编码的文件
# 事件挂钩
# 自定义身份验证
# AuthBase --> HTTPBasicAuth HTTPDigestAuth
#
#
# 编码的合规性
#
# >>> from requests.auth import HTTPBasicAuth
# >>> auth = HTTPBasicAuth('fake@example.com', 'not_a_real_password')
# >>> r = requests.post(url=url, data=body, auth=auth)
# >>> r.status_code
#
# 定制动词
# requests.request('MKCOL', url, data=data)
#
# 响应头链接字段
# 许多HTTP API都有响应头链接字段的特性，使得API能够更好地自我描述和自我显露
#
# 阻塞和非阻塞


# 超时(timeout)
# 为防止服务器不能及时响应，大部分发至外部服务器的请求都应该带着timeout参数
# 连接超时指的是客户端实现到远端机器端口的连接时(对应的是connect)，Request会等待的秒数
# 读取超时指的是客户端等待服务器发送请求的时间(在 99.9% 的情况下这指的是服务器发送第一个字节之前的时间)
r = requests.get('https://github.com', timeout=5)           # connect和read二者的timeout
r = requests.get('https://github.com', timeout=(3.05, 27))  # connect和read分开
