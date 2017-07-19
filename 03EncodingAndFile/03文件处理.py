#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com


##################文件以读 r 模式打开文件########################

# f = open('a.txt', mode='r', encoding='utf-8')  # # 发系统调用，中文Windows默认GBK
# # print(f)  # 文件对象<_io.TextIOWrapper name='a.txt' mode='r' encoding='utf-8'>
# data1 = f.read()
# print(data1)
#
# data2 = f.read()
# print('data2====>', data2)  # 读不到内容
#
# f.close()
#
#
# f = open('a.txt', mode='r', encoding='utf-8')
# f.read()
# f.seek(0)         # 光标移到开始
# data3 = f.read()  # 再读就又有值了
# print('data3====>', data3)
#
# f.close()
#
#
# f = open('a.txt', mode='r', encoding='utf-8')
# print(f.closed)       # 判断文件是否是关闭状态
# print(f.encoding)
# print(f.name)
# print(f.readable())   # 判断文件是否是r模式打开的
# f.close()
# f = open('a.txt', mode='r', encoding='utf-8')
# print(f.readline(), end='')  # 一次读一行，其中print函数默认end='\n'
# print(f.readline(), end='')  # end=''表示print函数末尾为空，最终效果还原文档格式
#
# print(f.readlines())         # 读取所有行的内容，存成列表的形式
# f.close()


##################文件以读写 w 模式打开文件########################
# f = open('a.txt', mode='w', encoding='utf-8')  # 有则清空；无则创建

# f = open('b.txt', mode='r', encoding='utf-8')  # 以读的方式打开文件，文件不存在则报错
# f = open('b.txt', mode='w', encoding='utf-8')  # 以写的方式打开文件，文件不存在则创建
# print(f.writable())
# f.write('11111\n22222\n')
# f.write('33333\n44444\n')
#
# f.writelines(['55555\n', '66666\n', '77777\n'])  # 参数为列表形式
# f.close()


##################文件的修改########################
# linux swap 交换文件

f_read = open('b.txt', mode='r', encoding='utf-8')
f_write = open('b_swap.txt', mode='w', encoding='utf-8')

for line in f_read.readlines():
    if line.startswith('2222'):
        line = 'xxxxx\n'
    f_write.write(line)
f_read.close()
f_write.close()
import os
os.remove('b.txt')
os.rename('b_swap.txt', 'b.txt')
