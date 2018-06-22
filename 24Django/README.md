## Django 前言

### Web应用介绍

Socket  多个Client端，单个服务端
* 客户端世界各地、不定时、大批量访问
* 客户端是运行在客户电脑上的软件
* 服务端24小时运行
* 服务端是运行在服务器上的软件

浏览器是用于发web请求的客户端，Socket套接字对象

HTTP协议 是基于请求/访问的网络协议，有请求才有响应


```
conn.send(b"<h1>Hello World</h1><img src='https://bd.static.com/a.jpg'>")

```

### HTTP请求协议与响应协议

- 请求协议是对客户端规定的协议，如约束浏览器
- 响应协议是对服务端规定的协议

#### 请求协议

```
请求首行
POST /form/entry HTTP/1.1\r\n

请求首部字段
Host: jonathan.com\r\n
Connection: keep-alive\r\n  # close 响应结束立刻断开; keep-alive 3000ms
Content-Type: application/x-www-form-urlencoded\r\n
Content-Length: 16\r\n\r\n


内容实体
name=alex&age=18
```

* POST请求才会有请求体
* 首行与请求首部\r\n隔开
* 头与请求体\r\n\r\n隔开


#### 响应协议
```
响应首行
HTTP/1.1 200 OK    # 协议版本 状态码 状态码的原因短语
响应首部字段
Date: Tue, 10 Jul 2012 06:50:15 GMT
Content-Length: 362
Content-Type: text/html

<html>...
```

#### 重定向



#### URL
协议://IP:端口(8080)/路径/?a=1&b=2


* 按照HTTP请求协议解析数据
* 中间专注web业务开发
* 按照 HTTP响应协议封装数据
```
正确的做法底层代码由专门的服务器软件实现，如TCP连接、HTTP原始请求和响应格式
所以需要一个统一的接口协议来实现这样的服务器软件，我们专心用Python编写Web业务，这个接口就是WSGI: Web Server Gateway Interface,
而wsgiref模块就是Python基于wsgi协议开发的服务模块

```



### DIY Web 框架

```
1. urls.py      # 路径与视图函数映射关系                --> url控制器
2. views.py     # 视图函数，固定有一个形式参数：environ，封装请求数据
3. templates    # HTML文件                              --> 模板
4. models.py    # 在项目启动前，在数据库中创建表结构    --> 与数据库相关

main.py         # 启动文件，封装socket
```

## Django

### 项目目录

```
pip install django==2.0.1
import sys
sys.path

mysites             # 项目相关
  - settings.py     # 项目配置
  - urls.py         # url总入口
manage.py           # Django调试工具，调用Shell和数据库
blog                # 应用相关
  - models.py       # 数据模型
  - views.py        # 视图函数
templates           # HTML文件
```


### 静态文件

```
1. Django中静态文件
statics
  - js
    - jquery.js
    
2. Django中settings配置
settings.py
STATIC_URL = '/static/'                             # 前端静态文件别名
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "statics"),              # 实际的文件statics
]

3. Django中网页文件排位置
templates
  - index.html
  
<script src='static/js/jquery.js'></script>           # 设置的也是static别名

4. 实际访问 http://127.0.0.1:8000/static/js/jquery.js # 访问的是别名

```

js、css等静态文件浏览器会自动请求加载

### url控制器
* 若要从url中捕获一个值，只需要在它周围放置一对圆括号
* 不需要添加一个前导的反斜杠，因为每个url都有
* 每个正则表达式前面的'r'是可选的但建议加上，它告诉Python这个字符串是 "原始的" -- 字符串中任何字符都不应该有转义


```
from django.conf.urls import url

from django.urls import path
```

### 反向解析

```
{% url 'LOGIN' %}

return redirect(reverse('LOGIN'))

```

### 命名空间



### Content-Type

```
请求首行
请求头部字段 Content-Type  --> 决定请求体以什么格式封装数据

请求体

如form表单 entype可以有如下两种
application/x-www-form-urlencoded   --> a=1&b=2
multipart/form-data                 --> 文件

Ajax提交格式
application/json

```

### Cookie

HTTP请求协议的无状态保存

会话：在多次HTTP请求之间保存相关信息，来弥补请求协议的无状态保存

Cookie：具体一个浏览器针对一个服务器存储 key-value({})

如当登录认证完成后，下次请求可携带已登录的key:value，可实现已登录后的请求了



#### 应用Cookie

```
响应体 --> 本质都是HttpResponse()
return HttpResponse()
return render()
retrun redirect()

# 设置
if user == 'alex' and pwd == '123':
    response = HttpResponse('登录成功')
    response.set_cookie('is_login', True)
    response.set_cookie('username', user)
    return response

# 使用
is_login = request.COOKIES.get('is_login')
username = ''
if is_login:
    username = request.COOKIES.get('username')
    

注意三个问题：
1. 一次登录成功，设置好set_cookie，再访问时都会带着这个cookie
2. 当换一个浏览器时，cookie重新开始
3. 当前浏览器访问其他服务器时，原先服务器的cookie不会被携带

```

#### 设置有效期
```
max_age = 浏览器存储cookie时间段 单位s
expires = 指定浏览器存储cookie在特定时刻 失效
path = '/index' 指定特定路径有效

response.set_cookie('is_login', True, max_age=3000)
response.set_cookie('username', user, expires=datetime.datetime(2019, 5, 1))
response.set_cookie('username', user, path='/index')
response.delete_cookie('username')
```


### Session

会话跟踪技术

```
request.session['login'] = True
request.session['user'] = 'tom'
"""
1. 生成随机字符串 '345djigjdjijagid'
2. response.set_cookie('sessionid', '345djigjdjijagid')
3. 在django_session表中创建一条记录：
    session_key         session_data
    345djigjdjijagid    {"is_login": True, "username": "linda"}
    
如果 reqeust.COOKIES.get('sessionid') 有值，更新即可
"""


"""
1. request.COOKIES.get('sessionid')  得到随机字符串 '345djigjdjijagid'
2. django_session 表中过滤记录 '345djigjdjijagid'
3. 取得 session_data
"""
print(dict(request.session))


request.session.flush()    删除当前的会话数据并删除会话的Cookie，执行如下操作
random_str = request.COOKIES.get('sessionid')
django_session.objects.filter(session_key=random_str).delete()
response.delete_cookie('sessionid')
```


#### 语句总结

* resoponse.set_cookie(key,value)

* request.COOKIES.get(key)

* reqeust.session[key] = value   注意Django的处理流程

* request.session.get(key)

* requsst.session.flush()



两个不同级别用户登录时，发生更新覆盖，会产生问题  -- auth 模块


### auth

用户认证组件

功能：用session记录登录验证状态

前提：必须用Django自带的表auth_user

创建超级用户：python manage.py createsuperuser


```
from django.contribute import auth
1. user = auth.authenticate(username=username, password=pwd)       
# if验证成功返回user对象，否则返回None
2. auth.login(request, user)       # request.user 当前登录对象
3. auth.logout(request)

from django.contribute.auth.models import User
4. request.user.is_authenticate
5. User.objects.create_user(username=username, password=password)

匿名用户对象

if 没有执行 auth.login(request, user)   request.user == AnonymousUser()
else 执行 auth(reqeust, user)           request.user == 登录对象
request.user，是全局变量，在任何视图和模板中直接使用


```


#### 装饰器
```
from django.contribute.auth.decorators import login_required

@login_required
def func(req):
    pass

LOGIN_URL = '/login/'
```


### 参考链接

```
2 http协议	
https://www.cnblogs.com/yuanchenqi/articles/8875623.html

3 web框架
https://www.cnblogs.com/yuanchenqi/articles/8946917.html

4 Django简介
https://www.cnblogs.com/yuanchenqi/articles/8875659.html

5 Django-2的路由层(URLconf)
https://www.cnblogs.com/yuanchenqi/articles/8931472.html

6 Django的视图层
https://www.cnblogs.com/yuanchenqi/articles/8876856.html


13 Django组件 cookie与session
https://www.cnblogs.com/yuanchenqi/articles/9036467.html


11 Django的用户认证组件
https://www.cnblogs.com/yuanchenqi/articles/9064397.html

12 Django组件-中间件
https://www.cnblogs.com/yuanchenqi/articles/9036479.html
```