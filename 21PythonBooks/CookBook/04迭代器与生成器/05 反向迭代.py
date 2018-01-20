#!/usr/bin/env python
# -*-coding:utf-8 -*-

a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)


# reversed()反向迭代仅仅当对象的大小可预先确定或对象实现了__reversed__()的特殊方法才能生效
# 如果两者都不符合，必须先将对象转换成一个列表才行
f = open('test', 'r')
for line in reversed(list(f)):
    print(line, end='')
f.close()

# 如果可迭代对象元素很多的话，将其预先转换为一个列表将消耗大量的内存
# 可咋已定义类上实现__reversed__()方法来实现方向迭代


class Countdown(object):
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for rr in reversed(Countdown(10)):
    print(rr)


print('-----------我是分割线------------')
for rr in Countdown(5):
    print(rr)

"""
1. __iter__(),__reversed__(),是属于触发的代理接口，具体实现还得自己写代码
2. 定义一个反向迭代器可以使代码非常高效，因为不需要将数据填充到一个列表中然后再去反向迭代这个列表
"""