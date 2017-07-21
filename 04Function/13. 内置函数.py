#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

print(abs(-1))
print(all([1, 2, 3]))
print(all(''))  # 空的也是 True

print(any([0, None, '', 1]))  # True
print(any([]))     # False

print(bin(3))   # 十进制转二进制     0b11
print(hex(10))  # 十进制转十六进制  0xa
print(oct(9))   # 十进制转八进制    0o11

# 0 None 空 ===》 bool值为False


def func():
    pass
print(callable(func))

print(chr(68))    # D   ascii 表 数字 ==> 字符
print(ord('D'))  # 68

"""
# 数据类型  工厂函数
dict
int
str
set
list
"""

l = [1, 2, 3]
print(dir(l))   # 查看一个对象下面的属性
print(help(l))  # 使用介绍

print(divmod(100, 3)) # (商，余) 实现分页功能

enumerate([1, 2, 3]).__next__() # 迭代器

cmd = 'print("您好")'
eval(cmd)

dic = "{'a':1, 'b':2}"
d = eval(dic)
print(type(d))

with open('user.db', 'w', encoding='utf-8') as f:
    user_dic = {'name': 'Linda', 'password': '123456'}
    # f.write(user_dic) # TypeError: write() argument must be str, not dict
    f.write(str(user_dic))

# 从user.db读出字符串，可用eval() 生成字典

s = {1, 2}  # s = set({1, 2}   # 定义可变集合
s2 = frozenset({3, 4})         # 定义不可变集合

print(hash('abcddd'))
print(hash('abcddd'))

x = 1
y = x
print(id(x), id(y))
print(x is y)  # 身份运算符 is
print(x == y)  # == 判断的是值

print(max([1, 2, 4, 5]))

print(pow(10, 2))     # 10 ** 2
print(pow(10, 2, 3))  # 10 ** 2 / 3

print(reversed(['a',4, 2, 3]))      # <list_reverseiterator object at 0x0000009F4BC1A198>
for i in reversed(['a', 4, 2, 3]):
    print(i)
print(list(reversed(['a', 4, 2, 3])))

print(round(3.1415926, 3))  # 3.142 四舍五入

l = ['a', 'b', 'c', 'd', 'e']
s = slice(1, 4, 2)  # 切片可以重复利用，一般不这样用
print(l[s])

vars() # 等价于locals()
list1 = [1, 2, 3]

s = 'hello'
l = [1, 2, 3, 4, 5]
z = zip(s, l)  # z 迭代器
for i in z:
    print(i)

"""
('h', 1)
('e', 2)
('l', 3)
('l', 4)
('o', 5)
"""

# import time
# time 不是字符串
m = __import__('time') # 以字符串的形式导入模块
m.sleep(5)



"""
# 面向对象里讲
classmethod
staticmethod
property

delattr
hasattr
getattr
setattr

isinstance
issubclass

super
"""


"""
map
reduce
filter

max
min
zip的用法
sorted
lambda

"""