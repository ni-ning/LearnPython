# -*- coding:utf-8 -*-
"""
为其他对象提供一种代理以控制这个对象的访问
"""

from abc import ABCMeta, abstractmethod


# 抽象实体: 规定RealSubject, VirtualSubject, ProtectedProxy对外具有一致方法
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


# 实体
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        with open(filename, mode='r', encoding='utf-8') as f:
            self.content = f.read()

    def get_content(self):
        return self.content

    def set_content(self, content):
        with open(self.filename, mode='w', encoding='utf-8') as f:
            f.write(content)


subject = RealSubject('text.txt')   # 初始化就读取内容了，若文件较大会占用内存
subject.get_content()


# 代理
class VirtualSubject(Subject):

    def __init__(self, filename):
        self.filename = filename
        self.subject = None

    def get_content(self):
        if not self.subject:
            self.subject = RealSubject(self.filename)
        return self.subject.get_content()

    def set_content(self, content):
        if not self.subject:
            self.subject = RealSubject(self.filename)
        self.subject.set_content(content)


sub = VirtualSubject('text.txt')    # 没有读取内容
sub.get_content()                   # 需要的时候，才读取内容


class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.subject = RealSubject(filename)

    def get_content(self):
        return self.subject.get_content()

    def set_content(self, content):
        raise PermissionError('无写入权限')


"""
应用场景：
 - 远程代理：为远程的对象提供代理
 - 虚代理：根据需要创建很大的对象
 - 保护代理：控制对原始对象的访问，用于对象有不同访问权限时
 
优点：
 - 远程代理：可以隐藏对象位于远程地址空间的事实
 - 虚代理：可以进行优化，例如根据要求创建对象
 - 保护代理：允许在访问一个对象时有一些附加的内务处理
"""