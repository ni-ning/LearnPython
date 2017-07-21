#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
1. index(),home() 基础之上增加@auth 验证，并且保存验证结果
"""


login_user = {'user':None, 'status':False}


def auth(func):
    def wrapper(*args, **kwargs):
        if login_user['user'] and login_user['status']:
            res = func(*args, **kwargs)
            return res
        else:
            name = input(">>: ")
            password = input('>>: ')
            if name == 'Linda' and password == '123':
                login_user['user'] = "Linda"
                login_user['status'] = True
                print('Login successfully!')
                res = func(*args, **kwargs)
                return res
            else:
                print('Login Error')
    return wrapper


@auth
def index():
    print('welcome to index page')


@auth
def home(name):
    print('%s welcome to home page' % name)


index()
home('Linda')
