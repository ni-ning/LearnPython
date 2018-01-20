#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
消费者/接收方
"""
import time
import pika

# 认证信息
credentials = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.254.143", 5672, "/", credentials))
# 建立通道
channel = connection.channel()
# 创建队列
channel.queue_declare("task_queue")


# 订阅的回调函数这个订阅回调函数是由pika库来调用的
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print(body.count(b'.'))
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 定义消息预处理数量
channel.basic_qos(prefetch_count=1)

# 定义通道消费者参数
channel.basic_consume(callback,
                      queue="task_queue")

print(' [*] Waiting for messages. To exit press CTRL+C')
# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理。按ctrl+c退出。
channel.start_consuming()
