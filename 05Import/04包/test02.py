#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import glance.api.policy
# 执行glance.__init__.py
# 再执行api.__init__.py
# 最后执行 policy.py

glance.api.policy.get()

# import glance.api.policy.get 报错，导入时.左边必须是包，.是包的语法


