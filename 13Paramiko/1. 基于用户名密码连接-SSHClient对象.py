#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname='c1.salt.com',
            port=22,
            username='root',
            password='******')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')

"""
stdin, stdout, stderr = ssh.exec_command('sudo df')
stdin.write('root123456')
stdin.flush
"""

# 获取命令结果
res = stdout.read()
print(res.decode('utf-8'))

# 关闭连接
ssh.close()

