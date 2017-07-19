#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
f = open('a.txt', 'r+')  # 读写
f = open('a.txt', 'w+')  # 读写
f = open('a.txt', 'a+')  # 追加并且读
"""

# 自动关闭文件，上下文管理
with open('a.txt', mode='r', encoding='utf-8') as f, open('b.txt', mode='r', encoding='utf-8') as f2:
    print(f.read())
    print(f2.read())

# 补充内容
for i in range(3):
    print(i)
    continue
else:
    print("========>")
# for循环不被break打断，就执行else代码，保证for循环是完整循环了
# 如网络传输时，提示完全传输

# b格式打开，写入，bytes对应01二进制，不涉及字符编码问题
with open('c.txt', 'rb') as f:
    print(f.read())   # 欢迎您  -->   b'\xe6\xac\xa2\xe8\xbf\x8e\xe6\x82\xa8'
    # print(f.read().decode('utf-8'))  # decode --> 内存中unicode形式

with open('d.txt', 'wb') as f:
    f.write('哈哈哈'.encode('utf-8'))

# 引出如.jpg, .png形式的文件如何打开

# with open('xx.jpg', 'r') as f:  # 文本方式 r 读不了二进制文件
#     print(f.read())

with open('xx.jpg', 'rb') as f_read, open('oo.jpg', 'wb') as f_write:
    data = f_read.read()
    f_write.write(data)

