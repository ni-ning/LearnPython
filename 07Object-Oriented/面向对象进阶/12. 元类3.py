#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com


class Mymeta(type):

    def __init__(self, cls_name, cls_bases, cls_dic):
        # 控制 Foo的行为
        for key, value in cls_dic.items():
            if key.startswith('__'):
                continue
            elif not callable(value):
                continue
            elif not value.__doc__:
                raise TypeError('%s必须有注释' % key)

            print(key, value)

        super().__init__(cls_name, cls_bases, cls_dic)
        # type('Foo', (object,), {})


class Foo(metaclass=Mymeta):  # Foo=Mymeta(Foo, 'Foo', (object,), {})
    x = 1

    def f1(self):
        'f1 function'
        print('from f1')

    def f2(self):
        'f2 function'
        print('from f2')

Foo()
