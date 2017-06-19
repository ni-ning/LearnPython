#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 字典、列表相互嵌套应用
user_list = [
    {'name': 'alex', 'password': '123456', 'times': 1},
    {'name': 'linda', 'password': '123456', 'times': 1},
    {'name': 'eric', 'password': '123456', 'times': 1},
    {'name': 'jonathan', 'password': '123456', 'times': 1},
]

user = input('用户名：')
pwd = input('密码：')

flag = False
for item in user_list:
    if user == item['name'] and pwd == item['password']:
        flag = True
        break

if flag:
    print('登录成功')
else:
    print('登录失败')
