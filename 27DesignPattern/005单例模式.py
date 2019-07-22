# -*- coding:utf-8 -*-

'''
保证一个类只有一个实例，并提供一个访问它的全局访问点。
如 模块全局对象，其他场景如日志对象，数据库连接池
'''


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, value):
        self.value = value


a = MyClass(10)
b = MyClass(20)

print(a.value)      # 20
print(b.value)      # 20
print(a is b)       # True

'''
优点：
 - 对唯一实例的受控访问
 - 单例相当于全局变量，但防止了命名空间被污染
'''

'''
创建型模式小结：
 - 抽象工厂模式和建造者模式相比于简单工厂模式和工厂方法模式而言更灵活也更复杂
 - 通常情况下，设计以简单工厂模式或工厂方法模式开始，当你发现设计需要更大的灵活性是，则向更复杂的设计模式演化
'''