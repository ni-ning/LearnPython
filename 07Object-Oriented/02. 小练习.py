#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 需求1 统计实例化对象的个数

# count = 100000
class Foo:
    count = 0   # 类内部变量引用方式，Foo.count, obj.count

    def __init__(self, name):
        # global count
        # count += 1       # 全局的count
        # self.count += 1  # 对象自己的count
        Foo.count += 1
        self.name = name

obj1 = Foo('Linda')  # FOO.count+=1 FOO.count=1
obj2 = Foo('Tom')    # FOO.count+=1 FOO.count=2

print(Foo.count)
print(obj1.count)
print(obj2.count)

# print(count)  # 全局统计

# 需求2 定义学生类
# 面向对象的可扩展性，先定义一部分功能，根据需求逐次添加


class Student:
    tag = 'Good Student'

    def __init__(self, nid, name, age):
        self.nid = nid
        self.name = name
        self.age = age

    # 体会可扩展性的强大，加一个功
    def walk(self):
        print('%s is walking' % self.name)

s1 = Student('1000', 'Linda', 18)
s2 = Student('1001', 'Tom', 20)

print(s1.nid, s1.name, s1.age)
print(s2.nid, s2.name, s2.age)
s1.walk()


# 需求3 英雄联盟角色，对象的交互

class Garen:
    camp = 'Demacia'

    def __init__(self, nickname, life_value=200, aggressivity=100):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


class Riven:
    camp = 'Noxus'

    def __init__(self, nickname, life_value=100, aggressivity=200):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


g = Garen('Linda')
r = Riven('Tom')

print(r.life_value)
g.attack(r)  # 对象的交互，向g发送执行attack指令
print(r.life_value)
