#!/usr/bin/env python
# -*-coding:utf-8 -*-

import pandas as pd

source = [
    {'user_id': 'X001', 'custom_id': 'Jonathan', 'age': 28},
    {'user_id': 'X002', 'custom_id': 'Cathrine', 'age': 18},
    {'user_id': 'X001', 'custom_id': 'William', 'age': 48},
    {'user_id': 'X003', 'custom_id': 'Linda', 'age': 8}
]

df = pd.DataFrame(source)

print(df.empty)                                                     # df 是否为空

age_list = [18, 28]
df1 = df[df['age'].isin(age_list)]                                  # 类似SQL中的WHERE in

for k, v in df.groupby(df.user_id):
    print(k)                                                        # user_id的取值
    print(v)                                                        # 新的分组df
    print('形状为：%s， 记录数为：%s' % (v.shape, v.shape[0]))
    print(v.to_dict(orient="records"))                              # df --> 字典列表


columns = ['user_id', 'custom_id', 'age']
header = ['员工账号', '客户账号', '年龄']

file_name = 'output.xlsx'

writer = pd.ExcelWriter(file_name)                                  # 可定义多个sheet
df.to_excel(writer, sheet_name='sheet', index=False, encoding='utf-8', columns=columns, header=header)

writer.save()
