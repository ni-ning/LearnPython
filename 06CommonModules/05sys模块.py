#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import sys
print(sys.argv)  # 命令行参数List，第一个元素是程序本身路径

"""
# 命令行运行 python  E:\s17\06CommonModules\05sys模块.py --host 192.168.100.1 --port 8080
# 得到结果
['E:\\s17\\06CommonModules\\05sys模块.py', '--host', '192.168.1001.', '--port', '8080']


sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxsize        Python3中最大的Int值
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称
sys.modules[__name__]   获得当前模块名称，一切皆对象，可以反射了
"""

import sys, time

for i in range(50):
    sys.stdout.write('%s%% %s\r' % (int(round((i+1)/50, 2) * 100),'#'*i))     # \r 跳到行首
    sys.stdout.flush()
    time.sleep(0.1)

'''
注意：在pycharm中执行无效，请到命令行中以脚本的方式执行
'''
