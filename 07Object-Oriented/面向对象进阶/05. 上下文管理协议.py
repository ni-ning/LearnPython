#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com


class Foo(object):
    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')

# with时候执行 __enter__
with Foo() as x:
    print(x)
    print('===>')
    print('===>')
    print('===>')
    print('===>')
# 跳出with时 执行__exit__