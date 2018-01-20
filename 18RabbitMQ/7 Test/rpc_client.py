#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
RPC/Client端
"""
import pika
import uuid


# 定义菲波那切数列RPC Client类调用RPC Server
class FibonacciRpcClient(object):
    def __init__(self):
        # 添加认证信息
        credentials = pika.PlainCredentials("admin", "admin")
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.254.144", 5672, "/", credentials))
        # 添加一个通道
        self.channel = self.connection.channel()
        # 生成一个随机队列-定义callback回调队列
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        # 定义回调的通道属性
        self.channel.basic_consume(self.on_response,  # 回调结果执行完执行的Client端的callback方法
                                   no_ack=True,
                                   queue=self.callback_queue)
        # 这里注意我们并没有直接阻塞的开始接收消息了

    # Client端 Callback方法
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            # 定义了self.response = body
            self.response = body

    def call(self, n):
        # 定义了一个普通字段
        self.response = None
        # 生成了一个uuid
        self.corr_id = str(uuid.uuid4())
        # 发送一个消息
        self.channel.basic_publish(exchange='',   # 使用默认的Exchange,根据发送的routing_key来选择队列
                                   routing_key='rpc_queue',  # 消息发送到rpc_queue队列中
                                   # 定义属性
                                   properties=pika.BasicProperties(
                                         reply_to=self.callback_queue,  # Client端定义了回调消息的callback队列
                                         correlation_id=self.corr_id,  # 唯一值用来做什么的？request和callback 匹配用
                                         ),
                                   body=str(n))

        # 开始循环 我们刚才定义self.response=None当不为空的时候停止`
        while self.response is None:
            # 非阻塞的接受消息
            self.connection.process_data_events(time_limit=3)
        return int(self.response)

# 实例化对象
fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
# 发送请求计算菲波那切数列 30
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)