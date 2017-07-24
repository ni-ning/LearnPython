#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import pickle
dic = {
    "name": "Linda",
    "age": 18,
    "sex": "female",
}

print(pickle.dumps(dic),type(pickle.dumps(dic)))  # 结果为bytes格式 b'xxxxxxxxxxxxxxxxxxxxxxxx', ' <class 'bytes'>

with open('a.pickle', 'wb') as f:
    f.write(pickle.dumps(dic))

with open('a.pickle', 'rb') as f:
    d = pickle.loads(f.read())

print(d, type(d))   # {'sex': 'female', 'age': 18, 'name': 'Linda'} <class 'dict'>

# pickle的便捷写法
dic = {
    "name": "Linda",
    "age": 18,
    "sex": "female",
}
pickle.dump(dic, open('b.pickle', 'wb'))
d1 = pickle.load(open('b.pickle', 'rb'))
print(d1, type(d1))


#　pickle可以序列化Python任意的对象

import json
import pickle
def func():
    print('from func')
# json.dumps(func) # 报错，json不支持Python函数类型 TypeError: <function func at 0x000000164BE0C378> is not JSON serializable

# f = pickle.dumps(func)
# print(f) # b'\x80\x03c__main__\nfunc\nq\x00.'  可序列表

pickle.dump(func, open('c.pkl', 'wb'))
res = pickle.load(open('c.pkl', 'rb'))
print(res)
res()   # 函数比较特殊，只能序列化函数地址，若注释掉函数体，就不可以执行******

"""
数据流转：

内存中结构化的数据  <-->  pickle格式数据  <-->   bytes类型   <--> 保存到文件中或基于网络传输

Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
"""
