#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import paramiko

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='root', password='*******')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')
res = stdout.read()
print(res.decode('utf-8'))
transport.close()
