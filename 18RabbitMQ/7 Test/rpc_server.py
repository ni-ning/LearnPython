#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
RPC/Server端
"""
import pika
# 添加认证信息
credentials = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.254.144", 5672, "/", credentials))

# 添加一个通道
channel = connection.channel()
# 添加一个队列,这个队列在Server就是我们监听请求的队列
channel.queue_declare(queue='rpc_queue')


# 斐波那契计算
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


#  应答函数,它是我们接受到消息后如处理的函数替代原来的callback
def on_request(ch, method, props, body):
    n = int(body)
    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     # 返回的队列,从属性的reply_to取出来
                     routing_key=props.reply_to,
                     # 添加correlation_id,和Client进行一致性匹配使用的
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     # 相应消息/我们的处理结果
                     body=str(response))
    # 增加消息回执
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 每次预处理的请求个数/这个请求我没有处理完不要给我发了
channel.basic_qos(prefetch_count=1)
# 定义接收通道的属性/定义了callback方法,接收的队列,返回的队列在哪里？on_request 的routing_key=props.reply_to
channel.basic_consume(on_request, queue='rpc_queue')

# 开始接收消息
print(" [x] Awaiting RPC requests")
channel.start_consuming()