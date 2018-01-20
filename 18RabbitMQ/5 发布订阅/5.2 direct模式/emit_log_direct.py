#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
生产者/发送方
"""
import pika
import sys

# 添加RabbitMQ Server端认证信息
credentials = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.254.144", 5672, "/", credentials))

# 创建通道
channel = connection.channel()
# 声明Exchange 且类型为 direct
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

# 从调用参数中或去类型
severity = sys.argv[1] if len(sys.argv) > 2 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
# 发送消息指定Exchange为direct_logs,routing_key 为调用参数获取的值
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
# 打印信息
print(" [x] Sent %r:%r" % (severity, message))
# 关闭通道
connection.close()