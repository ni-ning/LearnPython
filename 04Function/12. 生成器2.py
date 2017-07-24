#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com


# 只要函数体内有关键字yield，就把yield后值返回，该函数就是生成器函数
def counter(n):
    print('start....')
    i = 0
    while i < n:
        yield i
        i += 1
    print('end....')

g = counter(5)
print(g)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # StopIteration

"""
yield的功能：
    1. 相当于为函数封装好__iter__和__next__方法
    2. return只能返回一次值，函数就终止了，
       而yield能返回多次值，每次返回都会将函数暂停，下一次next会从上一次暂停的位置继续执行
"""
print('<===================================>')
# tail -f a.txt | grep 'python' 模拟管道
import time
def tail(filepath):
    with open(filepath,encoding='utf-8') as f:
        f.seek(0, 2)
        while True:
            line = f.readline().strip()
            if line:
                yield line
            else:
                time.sleep(0.2)

# t = tail('a.txt')
# print(next(t))
# for line in t:
#     print(line)


def grep(pattern, lines):
    for i in lines:
        if pattern in i:
            print(i)

grep('python', tail('a.txt'))
