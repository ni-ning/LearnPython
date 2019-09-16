# -*- coding:utf-8 -*-
'''
monkey.patch_all() 自动实现单线程下IO检测与切换
'''
import gevent
from gevent import monkey
monkey.patch_all()
import time
import threading


def eat():
    print('eat food 1')
    time.sleep(3)
    print('eat food 2')
    print('from eat: %s' % threading.current_thread().getName())


def play():
    print('play 1')
    time.sleep(4)
    print('play 2')
    print('from play: %s' % threading.current_thread().getName())


# 异步调用
g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)

gevent.joinall([g1, g2])
print('from main: %s' % threading.current_thread().getName())