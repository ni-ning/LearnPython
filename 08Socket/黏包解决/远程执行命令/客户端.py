#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
import socket
import struct
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))  # 建立连接--> 对应服务端 s.accept()
while True:  # 通信循环
    cmd = input('>>: ').strip()
    if not cmd: continue   # 防止客户端发空
    client.send(cmd.encode('utf-8')) # 发消息-->  对应服务端 s.read()

    """
    # 报头只包含大小的方案
    head = client.recv(4)
    total_size = struct.unpack('i', head)[0]
    recv_size = 0
    data = b''
    while recv_size < total_size:  # total_size 1025=1024+1
        recv_data = client.recv(1024)
        data += recv_data
        recv_size += len(recv_data)

    print(data.decode('gbk'))   # subprocess结果默然编码为 平台编码 gbk
    """

    # 自定制包头方案
    # 先收报头的长度
    head_struct = client.recv(4)
    head_len = struct.unpack('i', head_struct)[0]

    # 再收报头bytes
    head_btyes = client.recv(head_len)
    head_json = head_btyes.decode('utf-8')
    head_dic = json.loads(head_json)

    # 最后根据报头里的详细取真实数据
    print(head_dic)
    total_size = head_dic['total_size']
    recv_size = 0
    data = b''
    while recv_size < total_size:  # total_size 1025=1024+1
        recv_data = client.recv(1024)
        data += recv_data
        recv_size += len(recv_data)

    print(data.decode('gbk'))  # subprocess结果默然编码为 平台编码 gbk
