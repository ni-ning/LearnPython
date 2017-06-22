#!/usr/bin/env python3
# -*-coding:gbk -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 测试环境为 python3.6

s = '林'
# 第一步：启动Python解释器
# 第二步：Python解释器,以gbk编码规则把 s = '林' 读到内存
# 第三步：内存中开辟一块空间，Python3中以unicode方式存储，u'林'，这是Python3如何识别字符串的数据类型问题

s2 = s.encode(encoding='utf-8')
# 执行过程中：unicode -->encode -->utf-8(bytes)

# utf-8(bytes) -->decode -->unicode
# s.decode('utf-8')  # 报错 'str' object has no attribute 'decode',unicode只能encode()

s3 = s2.decode()  # bytes 只能decode

print(s)
print(s2)
print(s3)

# 文件开头指定的编码，是Python3读取文件时加载到内存的编码
# Python3中字符串(str这种数据类型)都会识别为unicode的结果

# 执行过程中才有字符串概念

# Python3中两种形式的字符串
# str(即unicode, u'林'),
# bytes(即 str.encode()的结果，b'\xe6\x9e\x97')

# Python2中也有两种形式的字符串
#  str == bytes
# unicode
