#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# spam.py
print('from the spam.py')
money = 1000


def read1():
    print('spam模块：', money)


def read2():
    print('spam模块')
    read1()


def change():
    global money
    money = 0
