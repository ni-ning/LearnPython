#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
生产者/发送方
"""
import pika

# 远程主机的RabbitMQ Server设置的用户名密码
credentials = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.254.143', 5672, '/', credentials))

# 创建通道
channel = connection.channel()
# 声明队列task_queue,RabbitMQ的消息队列机制如果队列不存在那么数据将会被丢掉,下面我们声明一个队列如果不存在创建
channel.queue_declare(queue='task_queue')

# 在队列中添加消息
for i in range(100):
    message = '%s Meassage ' % i or "Hello World!"
    # 发送消息
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(delivery_mode=2, )) # 标记属性消息为持久化消息需要客户端应答
    # 发送消息结束
    print(" [x] Sent %r" % message)

# 关闭通道
channel.close()
