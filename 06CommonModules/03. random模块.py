#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import random

print(random.random())         # 大于0且小于1之间的小数
print(random.randint(1, 3))    # 大于等于1且小于等于3之间的整数
print(random.randrange(1, 3))  # 大于等于1且小于3之间的整数

proxy_ip = [
    '1.1.1.1',
    '1.1.1.2',
    '1.1.1.3',
    '1.1.1.4',
]
print(random.choice(proxy_ip))               # 随机筛选元素
print(random.sample([1, '23', [4, 5]], 2))  # 列表元素任意2个组合新列表

print(random.uniform(1, 3))    # #大于1小于3的小数

item = [1, 3, 5, 7, 9]
random.shuffle(item)  # 打乱item的顺序,相当于"洗牌"
print(item)


# 生成随机码
def v_code(n=5):
    res = ''
    for i in range(n):
        num = random.randint(0, 9)
        s = (chr(random.randint(65, 90)))
        add = random.choice([num, s])
        res += str(add)
    return res

print(v_code(6))



