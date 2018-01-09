#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com


# 有名函数
def func(x, y):
    return x + y
func(1, 2)

# f = lambda x, y: x+y
# print(f)
# res = f(1,2)
# print(res)
"""
1. 没有名字，使用完立刻回收
2. 有参数、有返回值
3. 场景逻辑简单
"""

# 求最大值的key
salaries = {
    'a': 1000,
    'b': 2000,
    'c': 100,
    'd': 50
}

# print(max(salaries))  # 比较的是key
# print(max(salaries.values()))

res = zip(salaries.values(), salaries.keys())
print(max(res)[1])


def func(k):
    return salaries.get(k)


print(max(salaries, key=func))  # 第一取得key，传递可func，作为比较值
print(max(salaries, key=lambda k: salaries.get(k)))


print(sorted(salaries))  # 默认排序，从小到大，key
print(sorted(salaries, reverse=True))
print(sorted(salaries, key=lambda k: salaries.get(k)))  # 按照value，从小到大输出key


x = 1000


def func():
    global x
    x = 0


func()

print(x)
# 在func()执行过程中，修改了外部状态


# 函数式编程，模拟数学上的函数概念；不会修改外部状态
"""
map()
reduce()
filter()
"""
list1 = ['alex', 'steven', 'egon']
res = map(lambda i: i+'_sb', list1)  # map()对可迭代对象，遍历操作
print(list(res))


from functools import reduce
list2 = [1, 2, 3, 4, 5]
print(reduce(lambda x,y:x+y, list2, 0))  # 无初始值，会pop第一值作为x


list3 = ['alex_sb', 'steven_sb', 'egon_sb', 'linda']
res = filter(lambda x:x.endswith('_sb'), list3)
print(list(res))
