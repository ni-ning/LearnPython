#!/usr/bin/env python
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 测试环境为 python2.7

# 第一种形式的字符串 str, 即bytes
s = '林'        # python2中，直接就为bytes格式了，默认encode()的编码为文件开头utf-8
print repr(s)   # '\xe6\x9e\x97' ，三个字节，可以说明为utf-8格式
print type(s)   # <type 'str'>    python2中  bytes == str

print s.decode('utf-8')


# 第二种形式的字符串 unicode
s1 = u'林'
print repr(s1)   # u'\u6797'

s1.encode('utf-8')
s1.encode('gbk')
s1.encode('shift_jis')

s2 = '林'
print s2.decode('utf-8').encode('gbk')     # Windows命令行终端可以正常显示，但PyCharm乱码
print s2.decode('utf-8').encode('utf-8')   # PyCharm命令行终端可以正常显示