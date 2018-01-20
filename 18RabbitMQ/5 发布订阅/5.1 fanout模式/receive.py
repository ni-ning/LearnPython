#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import pika

"""
1. 声明一个exchange，类型为fanout
2. 申明一个随机queue
3. 绑定exchang与queue
"""

# 连接RabbitMQ验证信息
credentials = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.254.144", 5672, "/", credentials))

# 建立通道
channel = connection.channel()

# Bindings Exchanges 接收消息
channel.exchange_declare(exchange='logs',
                         exchange_type="fanout")

# 使用随机队列/并标注消费者断开连接后删除队列
# 不需要维护一个队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue


# Queue 与 Exchanges绑定
channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


# 定义回调函数这个回调函数将被pika库调用
def callback(ch, method, properties, body):
    print(" [x] %r" % body)

# 定义接收消息属性
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

# 开始接收消息
channel.start_consuming()