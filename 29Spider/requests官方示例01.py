# -*- coding:utf-8 -*-

import requests

# 预览
# r = requests.get('https://api.github.com/user', auth=('ni-ning', '******'))
# print(r.status_code)
# print(r.headers)
# print(r.encoding)
#
# print(r.content)    # b''    --> bytes
# print(r.text)       # u''    --> str
# print(r.json())     # object --> dict
'''
- 无需手动为URL添加查询字串
- 不需要为POST数据进行表单编码
- Keep-alive和HTTP连接池的功能是100%自动化
'''

# requests功能特性，完全满足今日web的需求
'''
- Keep-Alive & 连接池
- 国际化域名和 URL
- 带持久 Cookie 的会话
- 浏览器式的 SSL 认证
- 自动内容解码
- 基本/摘要式的身份认证
- 优雅的 key/value Cookie
- 自动解压
- Unicode 响应体
- HTTP(S) 代理支持
- 文件分块上传
- 流下载
- 连接超时
- 分块请求
- 支持 .netrc
'''


# 发送请求 and 获取响应
# 获取Github的公共时间线, r为Response对象, 从中获取我们想要的信息
# r = requests.get('https://api.github.com/events')

# requests简单的API，可以明显看出HTTP请求的类型
# r = requests.post('http://httpbin.org/post', data={'key': 'value'})
# print(r.text)
# r.text自动解码来自服务器的内容，大多数unicode字符集都能被无缝地解码
# 甚至r.encoding属性来改变，r.text会根据新值来自动解码，也可以根据需要自己实现编码

# 成功调用r.json()并不意味着响应的成功，有的服务器会在响应中包含一个json对象，r.raise_for_status()或r.status_code来检查结果
# print(r.json())

# r = requests.put('http://httpbin.org/put', data={'key1': 'value1'})
# print(r.raise_for_status())
# r = requests.delete('http://httpbin.org/delete')
# print(r.content)
# r = requests.head('http://httpbin.org/get')
# print(r.reason)
# r = requests.options('http://httpbin.org/get')
# print(r.status_code)


# 获取原始套接字响应，r.raw，那请求中stream=True
# r = requests.get('https://api.github.com/events', stream=True)
# print(r.raw)    # <urllib3.response.HTTPResponse object at 0x000001F49B8F7DD8>
# print(r.raw.read(10))
# with open('raw', 'wb') as fd:
#     for chunk in r.iter_content(10 * 1024):
#         fd.write(chunk)
# Response.iter_content 比 raw对象更实用，并提供大小设置


# 定制请求头
# url = 'https://api.github.com/ni-ning'
# headers = {'user-agent': 'my-app/0.0.1'}
# r = requests.get(url, headers=headers)
'''
- auth=(参数)优先级 > .netrc 设置用户认证信息 > headers设置的授权信息
- 如果被重定向到别的主机，授权header就会被删除
- 代理授权 header会被url中提供的代理身份覆盖掉
- 在我们能判断内容长度的情况下，header中的Content-Length会被改写

Requests 不会基于定制 header 的具体情况改变自己的行为。只不过在最后的请求中，所有的 header 信息都会被传递进去
'''


# 发送一些编码为表单的数据，data=dict即可，发送编码时自动编码为表单形式
# payload = {'key1': 'value1', 'key2': 'value2'}
# payload = (('key1', 'value1'), ('key1', 'value2'))  # key值可以重复
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)


# 如果传递的不是表单数据，而是string， 可以直接发送出去
import json
payload = {'some': 'data'}
# r = requests.post('http://httpbin.org/post', data=json.dumps(payload))
# print(r.text)


# 新增功能
# r = requests.post('http://httpbin.org/post', json=payload)
# print(r.text)  # headers中含有 Content-Type": "application/json"


# 上传文件
# url = 'http://httpbin.org/post'
# files = {'file': open('logo.png', 'rb')}
# r = requests.post(url, files=files)
# print(r.text)


# 响应状态码
# r = requests.get('http://httpbin.org/get')
# print(r.status_code)
# print(r.status_code == requests.codes.ok)   # 状态码查询对象
# 发送了一个错误请求(4xx客户端错误，5xx服务器错误响应)
# bad_r = requests.get('http://httpbin.org/status/404')
# print(bad_r.status_code)
# bad_r.raise_for_status()    # requests.exceptions.HTTPError


# Cookie
# cookies = dict(cookies_are='working')
# r = requests.get('http://httpbin.org/get', cookies=cookies)
# print(r.text)

# Cookie的返回对象为RequestsCookieJar, 它的行为和字典类似，但接口更为完整，适合跨域名路径使用
# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'http://httpbin.org/cookies'
# r = requests.get(url, cookies=jar)
# print(r.text)   # '{"cookies": {"tasty_cookie": "yum"}}'


# 重定向与请求历史
# 除了HEAD, requests会自动处理所有重定向，响应对象的history列表记录Response对象类别
# r = requests.get('http://github.com', allow_redirects=False)
# print(r.url)
# print(r.status_code)
# print(r.history)
# for resp in r.history:
#     print(resp.status_code)


# 超时
# 告诉requests经过timeout参数设定的秒数时间后停止等待响应，基本上所有的生产代码都需要这个参数
# requests.get('http://github.com', timeout=0.1)
# timeout 仅对连接过程有效，与响应体的下载无关


# 错误与异常
# 遇到网络问题(如 DNS查询失败、拒绝连接等)时，requests会抛出ConnectionError异常
# http请求返回不成功的状态码，r.raise_for_status()会抛出一个HTTPError异常
# 请求超时，Timeout异常
# 请求超过了设定的最大重定向次数，抛出requests.exceptions.RequestException