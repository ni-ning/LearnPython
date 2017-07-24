#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import sys
print(sys.path)   # 执行的是 bin/start.py 中的sys.path
# 意味着 可以 导入 ATM 下的所有文件

from conf import settings

def run():
    print('from main')
    print('配置文件内容', settings.x, settings.y)


