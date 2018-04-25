#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
当创建的客户有大量字段时，并且部分必须验证的字段，可以自定义异常，来区分不同异常，从而实现扩展
"""

DEBUG = False


class CustomBaseException(Exception):
    def __init__(self, msg):
        super(CustomBaseException, self).__init__(msg)


class CustomParamException(CustomBaseException):
    def __init__(self, reason):
        super(CustomParamException, self).__init__(reason)


class CustomPermException(CustomBaseException):
    def __init__(self):
        super(CustomBaseException, self).__init__('perm forbidden')


if __name__ == '__main__':

    def perm_info():
        try:
            raise CustomPermException()
        except Exception as e:
            raise e

    def parse_info():
        perm_info()
        raise CustomParamException('该字段必填')

    try:
        parse_info()           # 函数封装，可以实现异常层级嵌套
    except CustomBaseException as e:
        if DEBUG:
            import traceback
            traceback.print_exc()
        if isinstance(e, CustomParamException):
            print(e.args[0])   # 实际项目开发时，可以返回该参数 e.args[0]
        elif isinstance(e, CustomPermException):
            print('用户未授权')  # 实际项目开发时，可以返回该参数 '用户未授权'