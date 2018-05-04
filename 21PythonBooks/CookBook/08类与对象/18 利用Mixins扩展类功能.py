#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
问题：你有很多有用的方法，想使用它们来扩展其他类的功能，但是这些类并没有任何继承的关系，因此不能简单的将这些方法放入到一个基类，然后被其他类继承
"""

# 假设想扩展映射对象，给它们添加日志、唯一性设置、类型检查等功能，可以定义一些混入类


class LoggedMappingMixin(object):
    """
    Add logging to get/set/delete operations for debugging
    """
    __slots__ = ()  # 混入类都没有实例变量，因为直接实例化混入类没有任何意义

    def __getitem__(self, key):
        print('Getting' + str(key))
        return super(LoggedMappingMixin, self).__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {key}={value}'.format(key=key, value=value))
        return super(LoggedMappingMixin, self).__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super(LoggedMappingMixin, self).__delitem__(key)


class SetOnceMappingMixin(object):
    """
    Only allow a key to be set once
    """
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError('key ' + str(key) + ' already set')
        return super(SetOnceMappingMixin, self).__setitem__(key, value)


class StringKeysMappingMixin(object):
    """
    Restrict keys to strings only
    """
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise KeyError('keys must be strings')
        return super(StringKeysMappingMixin, self).__setitem__(key, value)


"""
这些类单独使用起来没有任何意义
通过多继承来和其他映射对象混入使用
"""


class LoggedDict(LoggedMappingMixin, dict):
    pass


d = LoggedDict()

d['x'] = 23
print(d['x'])
del d['x']


from collections import defaultdict


class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass


d = SetOnceDefaultDict(list)
d['y'].append(2)
d['y'].append(3)
# d['y'] = 23  # KeyError: 'key y already set'


"""
混入类注意点：
首先，混入类不能被实例化使用
其次，混入类没有自己的状态信息，可以就是没定义__init__()方法，而使用了__slots__ = ()
"""

# 还有一种实现混入类的方式就是使用装饰器


def LoggedMapping(cls):
    """第二种方式：使用装饰器"""

    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print('Setting {key}={value}'.format(key=key, value=value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('Deleting  ' + str(key))
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls

@LoggedMapping
class LoggedDict(dict):
    pass


l = LoggedDict()
l['log'] = 'logging'