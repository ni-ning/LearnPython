#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
消费者/接收方
"""
import pika
import sys

# 添加RabbitMQ Server端认证信息
credentials = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.254.144", 5672, "/", credentials))

# 创建通道
channel = connection.channel()
# binding Exchange 为direct_logs, 且Exchange类型为direct
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

# 生成随机接收队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# 接收监听参数
severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

# 从循环参数中获取routing_key,并绑定
for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')


# 定义回调参数
def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

# 定义通道参数
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
# 开始接收消息
channel.start_consuming()