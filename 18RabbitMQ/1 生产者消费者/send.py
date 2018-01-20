#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
生产者/发送消息方
"""
import pika

# 远程主机的RabbitMQ Server设置的用户名密码
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.254.143', 5672, '/', credentials))

'''
ConnectionParameters 中的参数:virtual_host 注：
    相当于在rabbitmq层面又加了一层域名空间的限制,每个域名空间是独立的有自己的Echange/queues等
    举个好玩的例子Redis中的db0/1/2类似
'''

# 创建通道
channel = connection.channel()
# 声明队列hello,RabbitMQ的消息队列机制如果队列不存在那么数据将会被丢掉,下面我们声明一个队列如果不存在创建
channel.queue_declare(queue='hello')

# 给队列中添加消息
channel.publish(exchange="",       # 默认时，向routing_key="hello"，指定的队列发送消息
                routing_key="hello",
                body="Hello World")
print("向队列hello添加数据结束")
# 缓冲区已经flush而且消息已经确认发送到了RabbitMQ中，关闭通道
channel.close()