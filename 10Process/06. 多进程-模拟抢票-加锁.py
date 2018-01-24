#!/usr/bin/env python
# -*-coding:utf-8 -*-

from multiprocessing import Process, Lock
import random
import time
import json

"""
并发运行,效率高,但竞争同一打印终端,带来了打印错乱
加锁：由并发变成了串行,牺牲了运行效率,但避免了竞争
"""


def work(db_file, name, lock):
    lock.acquire()
    with open(db_file, mode='r', encoding='utf-8') as f:
        dic = json.loads(f.read())

    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(random.randint(1, 3))  # 模拟网络延迟
        with open(db_file, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(dic))
        print("\033[44m %s抢票成功\033[0m" % name)
    else:
        print("%s抢票失败" % name)
    lock.release()


if __name__ == '__main__':

    lock = Lock()
    p_l = []
    for i in range(100):
        p = Process(target=work, args=('db.txt', "用户%s" % str(i), lock))  # 并发执行，谁先准备好，就可以先抢到lock
        p.start()
        p_l.append(p)

    for p in p_l:
        p.join()

