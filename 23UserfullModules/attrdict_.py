#!/usr/bin/env python
# -*-coding:utf-8 -*-

from attrdict import AttrDict

a = AttrDict({'foo': 'bar'})

print(a.foo)
print(a['foo'])