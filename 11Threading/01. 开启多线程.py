#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from threading import Thread


# 开启线程1：继承Thread，实现run方法
class Work(Thread):
    def run(self):
        print("%s says hello." % self.name)


def work(name):
    print("%s says hello." % name)


if __name__ == '__main__':
    # 开启线程2：指定target
    t = Thread(target=work, args=('Linda',))
    t.start()   # 线程开销小，立刻执行

    t1 = Work()
    t1.start()

    print('主线程')