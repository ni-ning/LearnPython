# -*- coding:utf-8 -*-

from greenlet import greenlet


def eat(name):
    print('%s eat 1' % name)
    g2.switch('linda')
    print('%s eat 2' % name)
    g2.switch()


def play(name):
    print('%s play 1' % name)
    g1.switch()
    print('%s play 2' % name)


g1 = greenlet(eat)
g2 = greenlet(play)

g1.switch('alex')   # 第一次switch 传入参数，以后不需要

'''
greenlet 可以实现切任务，但是遇到IO，仍然会原地阻塞

单线程里20个任务的代码通常会既有计算操作又有阻塞操作，我们完全可以在执行任务1时遇到阻塞，就利用阻塞的时间去执行任务2......
如此，才能提高效率，这就用到了gevent模块
'''