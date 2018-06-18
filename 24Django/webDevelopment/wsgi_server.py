#!/usr/bin/env python3
# -*-coding:utf-8 -*-
from wsgiref.simple_server import make_server


def application(environ, start_response):
    # 按照http请求协议解析数据: environ
    # 按照http响应协议组装数据: start_response
    print(environ)
    print(type(environ))
    start_response('200 OK', [('Content-Type', 'text/html')])

    path = environ.get('PATH_INFO')
    if path == '/login':
        with open('login.html', 'r') as f:
            content = f.read()
        res = 'HTTP/1.1 200 OK\r\n\r\n%s' % content

    elif path == '/index':
        with open('index.html', 'r') as f:
            content = f.read()
        res = 'HTTP/1.1 200 OK\r\n\r\n%s' % content

    return [res.encode('GBK')]

    # return [b'<h1>Hello Web!</h1>']


# 封装socket
httpd = make_server("127.0.0.1", 8081, application)

# 等待用户连接: conn, addr = sock.accept()
httpd.serve_forever()   # 有请求来就调用 ---> application(environ, start_response)


