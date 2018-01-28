#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from threading import Thread
msg_li = []
format_li = []


# 交互
def talk():
    while True:
        msg = input(">: ").strip()
        if not msg:
            continue
        msg_li.append(msg)


# 格式化
def format():
    while True:
        if msg_li:
            res = msg_li.pop()
            format_li.append(res.upper())


# 保存
def save():
    while True:
        if format_li:
            txt = format_li.pop()
            with open('db.txt', 'a', encoding='utf-8') as f:
                f.write("%s\n" % txt)


if __name__ == '__main__':
    t1 = Thread(target=talk)
    t2 = Thread(target=format)
    t3 = Thread(target=save)
    t1.start()
    t2.start()
    t3.start()

