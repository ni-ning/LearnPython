#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
 一：函数对象：函数是第一类对象，即函数可以当作数据传递
    1 可以被引用
    2 可以当作参数传递
    3 返回值可以是函数
    4 可以当作容器类型的元素
"""


def foo():
    print('from foo')

# 1 可以被引用
func = foo
print(foo)
print(func)
func()


# 2 可以当作参数传递
def bar(func):
    print('from bar',func)
    func()
bar(foo)


# 3 返回值可以是函数
def poor(func):
    return func
poor(foo)()


# 4 可以当作容器类型的元素
dic = {'func': func}
dic['func']()


# 应用
def select(sql):
    print('=====> select',sql)


def insert(sql):
    print('=====> insert',sql)


def delete(sql):
    print('=====> delete',sql)


def update(sql):
    print('=====> update',sql)

func_dic = {
    'select': select,
    'insert': insert,
    'delete': delete,
    'update': update
}


def main():
    while True:
        sql = input('>>>: ').strip()
        if not sql: continue
        l = sql.split()
        cmd = l[0]
        if cmd in func_dic:
            func_dic[cmd](l)

main()
