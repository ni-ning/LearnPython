#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

#################################### int 整数 ####################################
age = 4
v1 = age.bit_length()    # 当前整数二进制最小位数  4 --> 3
v2 = age.to_bytes(10, byteorder='big')  # 获取当前数据的字节表示


#################################### bool 布尔值  ####################################
# 0，"", None, []  ----> False
# 1, " " , -1,     ----> True


#################################### list 列表  ####################################
user_list = ['Alex', 'Linda', 'Tom', 'Jonathan', 'Tim']  # 可变类型

# 1. 追加，是向 user_list 中追加
v = user_list.append('豆豆')
print(v)           # None
print(user_list)   # ['Alex', 'Linda', 'Tom', 'Jonathan', 'Tim', '豆豆']

# PS: name = 'alex' ,不可变类型

# 2. 清空
user_list.clear()  # []

# 3. copy 浅复制
user_list = ['Alex', 'Linda', 'Tom', 'Jonathan', 'Tim']
v1 = user_list.copy()

print(user_list)
print(v1)

# 4. 计数
user_list = ['Alex', 'Linda', 'Tom', 'Jonathan', 'Tim']
v2 = user_list.count('Tom')
print(v2)

# 5. 扩展
user_list = ['Alex', 'Linda', 'Tom']
user_list.extend(['Jonathan', 'Tim'])
print(user_list)

# 6. 查找索引,无元素时，报错
user_list = ['Alex', 'Linda', 'Tom', 'Jonathan', 'Tim']
v3 = user_list.index('Tim')
print(v3)

# 7. 按索引删除并且获取元素
user_list = ['Alex', 'Linda', 'Tom', 'Jonathan', 'Tim']
v4 = user_list.pop()
print("v4--> ", v4)

# 8. 按元素值删除,返回None
user_list = ['Alex', 'Linda', 'Tom', 'Jonathan', 'Tim']
user_list.remove('Linda')
print(user_list)

# 9. 反转
user_list = ['Alex', 'Linda', 'Tom', 'Jonathan', 'Tim']
user_list.reverse()
print(user_list)

# 10. 排序
nums = [11, 12, 9, 20, 1, 39, ]
nums.sort()  # 从小到大
nums.sort(reverse=True)  # 从大到小
print(nums)

######## 列表 额外功能
user_list = ['Alex', 'Linda', 'Tom', 'Jonathan', 'Tim']
user_list[0]
user_list[0::2]
del user_list[0]
for i in user_list:
    print(i)
user_list[0] = 'Eric'
user_list = [[], [], []]


# range(1,11)
# python2.7 --> [1,2,3,4,5,6,7,8,9,10]
# python3中做优化：具有生成连续整数的能力
for i in range(1,11):
    print(i)
for i in range(10, 0, -1):
    print(i)
# range，len，user_list
user_list = ['Alex', 'Linda', 'Tom', 'Jonathan', 'Tim']
for i in range(0, len(user_list)):
    print(i + 1, user_list[i])

# enumerate(可循环变量，起始值) --> 额外序号，元素值
for i, item in enumerate(user_list, 1):
    print(i, item)
