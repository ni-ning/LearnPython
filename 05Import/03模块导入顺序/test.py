#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import spam
import sys
print(sys.path)

"""
模块的搜索顺序
内存 ---->  内置 ----> sys.path
其中sys.path顺序为['文件所在当前目录', '项目的根目录', '.zip', 'DLLs', 'lib', 'python', 'sit-packages', '....']

"""

# 无论 import还是from...import.. 都是从当前文件目录出发，
# 想导入与当前文件目录评级的目录，需修改 sys.path路径
import sys
sys.path.append(r'c:\xxx')
print(sys.path)