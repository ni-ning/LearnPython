#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 类和对象关系
str1 = str('我是字符串')
list1 = list([1, 2, 3, 4])
dict1 = {'k1': 'v1'}

#################################### str 字符串 ####################################

name = 'alex'       # str类的对象，name

# capitalize()首字母变大写
# 自身不变，会生成一个新的值
name.capitalize()     # 自动找到name关联的str类，执行capitalize()功能
name.casefold()       # 除了英文，还可以处理其他外文类小写
name.lower()          # 只能处理为英文小写

name.center(20, '*')      # 第二个参数只能写一个字符

name = 'alexaaadddsdad'
v = name.count('ad')      # 子序列在字符串中出现的次数

name = 'alexddd'
name.endswith('dddd')    # 是否以xxx结尾
name.startswith('alex')  # 是否以xxx开始

name = 'al\tex\tdddd\nddd\tlex\tabd'
name.expandtabs(20)  # 把\t和\t签名的字符以特定长度展现

name = 'alex'
name.find('ex')   # 找不到 返回-1
# name.index('0') # 找不到 报异常 ValueError

tpl = "我是：{0};  年龄：{1};  性别:{2}"
v1 = tpl.format("李杰", 19, '男')

tpl = "我是：{name};  年龄：{age};  性别:{gender}"
v2 = tpl.format(name="李杰", age=19, gender='男')

tpl = "我是：{name};  年龄：{age};  性别:{gender}"
v3 = tpl.format_map({"name": "李杰", "age": 19, "gender": '男'})  # 参数为字典

name = 'alex33汉字'
name.isalnum()  # 数字、字母、汉字
name.isalpha()  # 字母、汉字

num = '②'
v1 = num.isdecimal()  # '123'，常用这个  int转换
v2 = num.isdigit()    # '123'，②
v3 = num.isnumeric()  # '123', ②, '二'

n = 'str'
n.isidentifier()    # 判定是否为合法变量
n.islower()         # 是否全部是小写
n.isupper()          # 是否全部是大写


str1 = 'alex\n'
str1.isprintable()  # 是否包含隐含非打印字符

name = '  '
name.isspace()      # 是否是空格

title = "This Is A Title"
title.istitle()

#  元素拼接
name = 'alex'
v = '_'.join(name)       # 内部循环每个元素  a_l_e_x

name_list = ['Alex', 'Linda', 'Tom']
v = '-'.join(name_list)  # 内部循环每个元素  Alex-Linda-Tom

# 'alex' + 123   字符串和数字是不能拼接的

# center,ljust,rjust 填充
name = 'alex'
name.ljust(20, '*')

