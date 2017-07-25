#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 多态：同一种事物的多种形态，如动物有人、狗、猪等多种形态

# 多态性：具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同功能的函数，如func(obj):pass

class Animal:
    def talk(self):
        print('叫...')


class People(Animal):
    def talk(self):
        print('啊啊啊')


class Pig(Animal):
    def talk(self):
        print('哼哼哼')


class Dog(Animal):
    def talk(self):
        print('汪汪汪')

peo1 = People()
pig1 = Pig()
dog1 = Dog()


def func(obj):
    obj.talk()


# 对于使用者来说，统一了调用方式
func(peo1)
func(pig1)
func(dog1)
