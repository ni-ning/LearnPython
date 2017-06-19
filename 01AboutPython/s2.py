#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 字符串
# bool转换
v = " "
print(bool(v))

# 移除空白
val = '   alex   '
print(val.strip())
print(val.lstrip())
print(val)

# 分割
user_info = "alex|sb123|9"
v1 = user_info.split("|", 1)
print(v1)
v2 = user_info.rsplit("|", 1)
print(v2)

# 长度, python3 按字符
val = '杰李sb'
print(len(val))

# 索引 按字符
val = '李杰sb'
print(val[3])

i = 0
while i < len(val):
    print(val[i])
    i += 1


# 切片
name = '我叫李杰，今年18岁，我在说谎！'
print(name[0:2])
print(name[5:9])
print(name[5:])
print(name[5:-1])
print(name[0:10:2])
print(name[0::2])
print(name[-2:])

