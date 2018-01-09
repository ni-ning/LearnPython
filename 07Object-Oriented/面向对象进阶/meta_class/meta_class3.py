#!/usr/bin/env python
# -*-coding:utf-8 -*-


# 定制元类实现单例模式
class Mymeta(type):

    # 定义类Mysql时触发
    def __init__(cls, cls_name, cls_bases, cls_dic):
        cls.__instance = None
        super(Mymeta, cls).__init__(cls_name, cls_bases, cls_dic)

    # 类Mysql(......)实例化时触发
    def __call__(cls, *args, **kwargs):

        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            cls.__init__(cls.__instance, *args, **kwargs)

        return cls.__instance


class Mysql(object, metaclass=Mymeta):
    def __init__(self, host='127.0.0.1', port=3306):
        self.host = host
        self.port = port


obj1 = Mysql()
obj2 = Mysql()

print(obj1 is obj2)



