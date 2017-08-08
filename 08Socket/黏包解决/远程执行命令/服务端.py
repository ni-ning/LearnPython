#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
import socket
import subprocess
import struct
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 8080))
s.listen(5)

while True:  # 链接循环，循环建链接
    print('starting...')
    conn, addr = s.accept()
    print('client addr', addr)

    while True:  # 与conn的通信循环
        try:
            cmd = conn.recv(1024)  # 收消息
            if not cmd: break     # Linux平台，不会报错，但会一直收空
            res = subprocess.Popen(cmd.decode('utf-8'),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            err = res.stderr.read()  # 管道只能读一次，返回值为 b''，编码为当前系统
            if err:
                cmd_res = err
            else:
                cmd_res = res.stdout.read()
            """
            # 报头只包含大小的方案
            conn.send(struct.pack('i', len(cmd_res)))  # 先发包头
            conn.sendall(cmd_res)                         # 再发真实数据
            """

            head_dic = {'filename': None, 'hash': None, 'total_size': len(cmd_res)}
            head_json = json.dumps(head_dic)
            head_bytes = head_json.encode('utf-8')

            # 先发报头的长度
            conn.send(struct.pack('i',len(head_bytes)))

            # 再发报头的bytes
            conn.send(head_bytes)

            # 最后发送真实数据
            conn.sendall(cmd_res)

        except ConnectionResetError as e:
            break
    conn.close()

s.close()
