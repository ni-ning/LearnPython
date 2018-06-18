#!/usr/bin/env python3
# -*-coding:utf-8 -*-

from DIY.views import *

url_patterns = [
    ('/login', login),          # url --> 视图函数
    ('/register', register),    # url --> 视图函数
    ('/logout', logout),        # url --> 视图函数
    ('/favicon.ico', fav),      # url --> 视图函数
]
