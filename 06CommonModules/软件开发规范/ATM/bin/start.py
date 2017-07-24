#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
"""
1. from .. 是包与模块的导入语法，而这个软件开发规范???
2. 软件的根目录 ATM 要放到sys.path里面去
"""

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)  # ATM目录已在搜索路径中

from core import main  # 但是PyCharm没有识别

if __name__ == '__main__':
    main.run()
