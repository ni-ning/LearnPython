#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa')

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='root', pkey=private_key)

sftp = paramiko.SFTPClient.from_transport(transport)
# 将test.txt上传至服务器 /application/test.txt
sftp.put('test.txt', '/application/test.txt')

# 将/application/test.txt 下载到本地 test01.txt
sftp.get('/application/test.txt', 'test01.txt')
transport.close()