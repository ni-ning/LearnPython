# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


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

