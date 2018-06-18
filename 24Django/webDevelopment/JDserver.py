#!/usr/bin/env python3
# -*-coding:gbk -*-
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8800))
sock.listen(5)

while True:
    print('server waiting...')
    conn, addr = sock.accept()  # conn 客户端的套接字对象
    data = conn.recv(1024)      # 浏览器传过来的内容，经过recv方法得到
    print('data', data)

    # conn.send(b'Hello World')   # 服务端没有按照标准的HTTP响应格式，浏览器解析不了，会报错
    # conn.send(b'HTTP/1.1 200 OK\r\n\r\n<h1>Hello World!</h1>')

    # with open('index.html', 'r') as f:
    #     content = f.read()
    with open('login.html', 'r') as f:
        content = f.read()

    res = 'HTTP/1.1 200 OK\r\n\r\n%s' % content
    conn.sendall(res.encode('GBK'))

    conn.close()

