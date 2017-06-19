#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 1. 打开并读取文件内容
f1 = open('db', 'r')
data = f1.read().strip()
f1.close()

# 2. 格式化，列表中嵌套字典
user_info_list = []
user_str_list = data.split('\n')
for item in user_str_list:
    temp = item.split('|')
    v = {
        'name': temp[0],
        'password': temp[1],
        'times': temp[2],
    }
    user_info_list.append(v)

# 登录操作
flag = False
times = 0
while times < 3:
    user = input('请输入用户名: ').strip()
    pwd = input('请输入密码: ').strip()

    for item in user_info_list:
        if item['name'] == user and item['password'] == pwd:
            print('登录成功！')
            flag = True
            break
    if flag:
        times += 1
        break
    else:
        times += 1


if not flag:
    print("%s登录次数达到%s,已被锁定" % (user, times))

    for item in user_info_list:
        if item['name'] == user:
            item['times'] = times
            break

    # 3. 重新拼接成字符串
    target_str = ""
    for user_dict in user_info_list:
        target_str = target_str + user_dict['name'] + '|' + user_dict['password'] + '|' + str(user_dict['times']) + '\n'

    # 4. 重新写入文件
    f2 = open('db', 'w')
    f2.write(target_str)
    f2.close()
