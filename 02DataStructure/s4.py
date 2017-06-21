#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

#####################  tuple 元组：不可修改的列表 #######################
user_tuple = ('Alex', 'Linda', 'Tom', 'Jonathan', 'Tim',)
# 1. 获取元素个数
v1 = user_tuple.count('Linda')

# 2. 获取元素索引
v2 = user_tuple.index('Linda')

# 元组额外功能
for item in user_tuple:
    print(item)

# user_tuple[0]
# user_tuple[0:2]

user_tuple1 = ('Alex', 'Linda', 'Tom', ['a', 'b', 'c'], 'Jonathan', 'Tim',)
# user_tuple1[3] = 111 元组元素是不可修改的
user_tuple1[3][0] = 1  # 注意要修改的时元组的元素还是列表的元素
print(user_tuple1)

###### 元组正确写法 (11,),最后有一个逗号



#################################  dict 字典 ##########################
# 1. 清空 clear
dic = {'k1': 'v1', 'k2': 'v2'}
dic.clear()  # {}

# 2. 浅拷贝
dic = {'k1': 'v1','k2': 'v2'}
dic.copy()

# 3.get('k1'),更新key获取相应value，不存在返回None
dic = {'k1': 'v1', 'k2': 'v2'}
dic.get('k1', 123)

# 4. pop('k1'),删除并获取对应的value值
dic = {'k1': 'v1', 'k2': 'v2'}
v1 = dic.pop('k1')

# 5. popitem()随机删除键值对，并获取删除的键值对k, v
dic = {'k1': 'v1', 'k2': 'v2'}
k, v = dic.popitem()
print(k, v)
print(dic)

# 6. setdefault() 增加，存在则不操作
dic.setdefault('k3', 'v3')
dic.setdefault('k1', '123456')
print(dic)

# 7. update() 批量增加或修改
dic.update({'k4': 'v4', 'k1': 'vvv1'})
print(dic)

# fromkeys() 注意第二个参数，是可变还是不可变；
dict1 = dict.fromkeys(['k1', 'k2', 'k3'], 123)
print(dict1)

dict2 = dict.fromkeys(['k1', 'k2', 'k3'], [1,])
print(dict2)
dict2['k1'].append(222)
print(dict2)
# {'k2': [1, 222], 'k1': [1, 222], 'k3': [1, 222]}

######## 字典额外功能
# 1. 字典可以嵌套
# 2. 字典key: 必须是不可变类型
dict3 = {
    'k1': 'v1',
    'k2': 'v2',
    (1, 2): 'v3',
    # [1, 2]: 'v3',  # TypeError: unhashable type: 'list'  --> 内部生成一个hash值
    True: True,
    123: True,
    1: 'hahah',      # 1就是True,并且比True作为key优先级高
}
print(dict3)


#####################  set 集合：不可重复的列表，可变类型 #####################

s1 = {'Alex', 'Eric', 'Linda', '李杰'}
s2 = {'Alex', 'Eric', 'Linda', '张三'}

# 1. s1中存在，s2中不存在
v = s1.difference(s2)
print(v)

# s1.difference_update(s2) 更新到s1

# 2. s2中存在，s1中不存在
v = s2.difference(s1)
print(v)

# 3.
# s1中存在，s2中不存在
# s2中存在，s1中不存在
v = s1.symmetric_difference(s2)
print(v)

# 4. 交集
v = s1.intersection(s2)
print(v)

# 5. 并集
v = s1.union(s2)
print(v)

# 6. 移除
s1.discard('Alex')
print(s1)

# 7. 更新
s1.update({'aaa', 'bbb', 'ccc'})
print(s1)

##### 额外功能
# 不支持索引
# 支持 for 循环
# 嵌套 只 支持 元组  {'12', 'ab', (1,3,4)}