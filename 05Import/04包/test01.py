#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import glance   # 执行glance.__init__.py

# glance.api.get.policy.get() # glance.__init__.py中没有相关文件，报错
print(glance.x)  # glance.__init__.py中定义了x，不会报错
print(glance.y)  # glance.__init__.py中定义了y，不会报错
