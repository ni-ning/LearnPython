#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):  # 开进程p1.start()就是调用self.run()
        print('%s is doing task' % self.name)
        time.sleep(3)
        print('%s has finished the task' % self.name)


if __name__ == '__main__':
    p1 = MyProcess('Linda')
    p1.start()     # p1.run()
    print('父进程')
