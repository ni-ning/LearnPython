#!/usr/bin/env python
# -*-coding:utf-8 -*-


# 函数接受任意数量的位置参数，*rest
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


print(avg(1, 2))
print(avg(1, 2, 3))


# 接受任意数量的关键字参数, **attrs
import html


def make_element(name, value, **attrs):
    keyvals = [" %s='%s'" % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name,
                                                       attrs=attr_str,
                                                       value=html.escape(value))
    return element


e1 = make_element('item', 'Albatross', size='large', quantity=6)
e2 = make_element('p', '<spam>')
print(e1)
print(e2)
