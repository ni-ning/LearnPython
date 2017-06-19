#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 列表
user_info = "alex|sb123|9"
v1 = user_info.split("|")
print(v1)

val = list(['alex', '狗', 'eric', 123, 'eric' ])
val.append('xxoo')   # 追加
print(val)
val.insert(0, '牛')  # 按索引值插入
print(val)

val.remove('eric')  # 按值删除，从左第一个
del val[0]          # 按索引删除
print(val)

val[1] = "母狗"     # 更新
print(val)


# for循环
for item in val:
    print(item)






