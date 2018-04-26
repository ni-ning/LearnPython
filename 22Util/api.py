#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
Web Service API， 后端接口封装
"""
from flask import jsonify


def get_error_msg(code):
    # 可以把status_code单独建立一个git目录，使用deploy-archive完成分发
    error_dict = {
        0: '成功',
        1: '未登陆',
        5: '未授权',
        10: '参数错误'
    }
    return error_dict.get(code, '未知错误')


class APIResult(dict):
    def __init__(self, code, result=None, msg=None):
        self['code'] = code
        self['msg'] = msg or get_error_msg(code)
        if result is None:
            result = {}
        self['result'] = result

    def jsonify(self):
        return jsonify(**self)

    def __call__(self, *args, **kwargs):
        return self.jsonify()


class api_wrap(object):

    def __init__(self, func):
        super(api_wrap, self).__init__()
        self._func = func
        self.__name__ = func.__name__

    def __get__(self, instance, owner):
        def wrap(*arg, **kw):
            return self._func(instance, *arg, **kw)
        wrap.__name__ = self._func.__name__
        return wrap

    def __call__(self, *arg, **kw):
        res = self._func(*arg, **kw)
        if isinstance(res, APIResult):
            return res.jsonify()
        return res


if __name__ == '__main__':

    from flask import Flask
    app = Flask(__name__)

    @app.route('/func/')
    def func():
        result = [{'_id': '001', 'name': 'Linda', 'age': 18, 'sex': False},
                  {'_id': '002', 'name': 'Tom', 'age': 28, 'sex': True},
                  {'_id': '003', 'name': 'Catherine', 'age': 38, 'sex': False}]

        return APIResult(0, result=result)()   # 这种方式调用需要两次括号，APIResult()()

    @app.route('/foo/')
    @api_wrap
    def foo():
        return APIResult(0, 'Success')         # 直接APIResult() 即可


