#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 继承的实现顺序

"""
    E   D
    A   B   C
        F
"""
class E:
    # def test(self):
    #     print('from E')
    pass

class A(E):
    # def test(self):
    #     print('from A')
    pass

class D:
    def test(self):
        print('from D')

class B(D):
    def test(self):
        print('from B')

class C:
    def test(self):
        print('from C')

class F(A, B, C):
    # def test(self):
    #     print('from F')
    pass

f = F()
f.test()

# 从左到右，一个一个分支遍历

"""
        A
    B       C
    D       E
        F
新式类：F -> D -> B -> E -> C ->A， 广度优先
"""
print(F.mro()) # Python 提供继承顺序方法



# 子类调用父类方法  super(Bar, self).test()，新式类按照mro顺序检索
class Foo:
    def test(self):
        print('from Foo')


class Bar(Foo):
    def test(self):
        # Foo.test(self)  # 若Foo名称变化，所有的子类都得跟着变化
        super(Bar, self).test()
        print('from Bar')

b = Bar()
b.test()


