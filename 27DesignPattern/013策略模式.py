# -*- coding:utf-8 -*-
'''
定义了一些列的算法，把它们一个个封装起来，并且使它们可相互替换
本模式使得算法可独立于使用它的客户端而变化
'''

from abc import ABCMeta, abstractmethod


# 抽象策略
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


# 具体策略
class FastStrategy(Strategy):
    def execute(self, data):
        print('用较快的策略处理: %s' % data)


# 具体策略
class SlowStrategy(Strategy):
    def execute(self, data):
        print('用较慢的策略处理: %s' % data)


# 上下文
class Context(object):
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


# Client
data = ['user1', 'user2', 'user3']
s = FastStrategy()
context = Context(s, data)
context.do_strategy()

s2 = SlowStrategy()
context.set_strategy(s2)
context.do_strategy()

'''
优点：
 - 定义了一系列可重用的算法和行为
 - 消除了一些条件语句
 - 可以提供相同行为的不同实现
 
缺点：
 - 客户必须了解不同的策略
'''