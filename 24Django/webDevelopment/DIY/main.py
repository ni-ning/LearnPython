#!/usr/bin/env python3
# -*-coding:utf-8 -*-
from wsgiref.simple_server import make_server
from DIY.urls import url_patterns


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    # 当前请求路径
    path = environ.get('PATH_INFO')

    # 方案一
    # if path == '/favicon.ico':
    #     with open('favicon.ico', 'rb') as f:
    #         ico = f.read()
    #     return [ico]
    #
    # elif path == '/login':
    #     return [b'Login']
    #
    # elif path == '/register':
    #     return [b'Register']
    #
    # elif path == '/logout':
    #     return [b'Logout']
    #
    # return [b'Hello Web']

    # 方案二 路由分发

    func = None
    for item in url_patterns:
        if path == item[0]:
            func = item[1]
            break
    if func is None:
        return [b'404!']
    else:
        return [func(environ)]

httpd = make_server('127.0.0.1', 8090, application)
httpd.serve_forever()

