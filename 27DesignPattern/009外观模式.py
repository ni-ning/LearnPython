# -*- coding:utf-8 -*-
'''
为子系统中的一组接口提供一个一致的界面，外观模式定义了一个高层接口
这个接口使得这一子系统更加容易使用
'''


# 子系统类
class CPU(object):
    def run(self):
        print('CPU 开始运行')

    def stop(self):
        print('CPU 结束运行')


class Disk(object):
    def run(self):
        print('磁盘 启动')

    def stop(self):
        print('磁盘 制动')


class Memory(object):
    def run(self):
        print('内存 通电')

    def stop(self):
        print('内存 断电')


# 外观(facade)
class Computer(object):
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


c = Computer()
c.run()
c.stop()

'''
优点：
 - 减少系统相互依赖
 - 提高了灵活性
 - 提高了安全性
'''