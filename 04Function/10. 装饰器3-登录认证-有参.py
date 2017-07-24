#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import time


def timmer(func):
    def wrapper(*args, **kwargs):
        print('===>timmer_wrapper')
        star_time = time.time()
        res = func(*args, **kwargs)  # func == auth2_wrapper
        stop_time = time.time()
        print('run time is %s' % (stop_time - star_time))
        return res
    return wrapper

login_user = {'user':None, 'status':False}


def auth(driver='file'):
    def auth2(func):
        def wrapper(*args, **kwargs):
            print('====>auth2_wrapper')
            if driver == 'file':
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
            elif driver == 'mysql':
                print('=====> mysql')
                res = func(*args, **kwargs)
                return res
            elif driver == 'ladp':
                print('=====> ladp')
                res = func(*args, **kwargs)
                return res
        return wrapper
    return auth2


@timmer  # index=timmer(time_wrapper)
@auth(driver='file')   # @auth2，包含对driver='file'的引用  ==> index=auth2(index)，包含对driver='file'的引用
def index():
    print('welcome to index page')


@auth(driver='file')  # @auth2，包含对driver='file'的引用  ==> home=auth2(home)，包含对driver='file'的引用
def home(name):
    print('%s welcome to home page' % name)


index()         # timmer_wrapper()
home('Linda')  # timmer_wrapper('Linda')