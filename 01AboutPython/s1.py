#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com


# a = "你好，我来自火星！"
# print(a)

# import getpass
# pwd = getpass.getpass("请输入密码：")
# print(pwd)


# getpass 命令行密文
import getpass
name = input("请输入用户名：")
pwd = getpass.getpass("请输入密码：")

if name == "alex" and pwd == "sb":
    print('欢迎登陆！')
else:
    print('滚蛋！')


# 三次机会登陆
count = 0
while count < 3:
    name = input("请输入用户名：")
    pwd = input("请输入密码：")

    if name == 'alex' and pwd == 'sb':
        print('登陆成功！')
        break
    else:
        print('用户名或密码错误，请重新输入...')
        count += 1

print('end...')
