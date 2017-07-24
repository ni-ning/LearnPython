#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import time

#  一： 三大类时间：时间戳、结构化时间、格式化字符串时间
# 1. 时间戳
# 时间戳是指格林威治时间1970年01月01日00时00分00秒(北京时间1970年01月01日08时00分00秒)起至现在的总秒数
print(time.time())
# 给计算机用

# 2. 结构化时间
# 给人用，本地时间对象
print(time.localtime())
# print(time.localtime().tm_year)  # 2017

# 标准时间对象，差八个小时
print(time.gmtime())

# 3. 格式化的字符串
print(time.strftime('%Y-%m-%d %H:%M:%S'))


#  二： 三种格式之间的转换
# 1. 时间戳Timestamp <--> 结构化时间 struct_time
print(time.localtime(1500800674.1920106))  # 时间戳Timestamp --> 结构化时间 struct_time
print(time.mktime(time.localtime()))       # 结构化时间 struct_time -->  时间戳Timestamp


# 2. 格式化字符串时间 format string  <-->  结构化时间 struct_time
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))         # 结构化时间 struct_time -->   格式化字符串时间 format string
print(time.strptime('2017-07-23 17:19:22', '%Y-%m-%d %H:%M:%S'))  # 格式化字符串时间 format string -->  结构化时间 struct_time


# 3. 时间戳或结构化时间 --->  Linux当中时间格式
print(time.ctime(time.time()))         # Sun Jul 23 17:26:14 2017
print(time.asctime(time.localtime()))  # Sun Jul 23 17:26:33 2017