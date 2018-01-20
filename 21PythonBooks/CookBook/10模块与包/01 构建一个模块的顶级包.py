#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
封装成包，类似文件系统组织，确保每个目录定义了__init__.py文件
graphics/
    __init__.py
    primitive/
        __init__.py
        line.py
        fill.py
        text.py
    formats/
        __init__.py
        png.py
        jpg.py
"""

# import graphics.primitive.line
# from graphics.primitive import line
# import graphics.formats.jpg as jpg

"""
执行 import graphics，则文件graphics/__init__.py将被导入，建立graphics命名空间内容

import graphics.format.jpg，那么
文件graphics/__init__.py和文件graphics/formats/__init__.py将在文件graphics/formats/jpg.py导入之前导入
"""

# 绝大部分时候让__init__.py空着就好，也可以有内容，如自动加载子模块
"""
# graphics/formats/__init__.py
from . import jpg
from . import png
"""
# 就可以通过import grahpics.formats 代替import graphics.formats.jpg和import graphics.formats.png

# __init__.py的其他常用用法包括将多个文件合并到一个逻辑命名空间

