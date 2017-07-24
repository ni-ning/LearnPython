#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import os
import sys
# OS模块是与操作系统交互的一个接口

"""
os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
os.curdir  返回当前目录: ('.')
os.pardir  获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')    可生成多层递归目录
os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  删除一个文件
os.rename("oldname","newname")  重命名文件/目录
os.stat('path/filename')  获取文件/目录信息
os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep    输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"
os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:
os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'

"""

print(os.path.abspath('a.txt'))           #  返回path规范化的绝对路径， E:\s17\06CommonModules\a.txt
print(os.path.abspath('/a.txt'))         # E:\a.txt
print(os.path.split('E:\\a.txt'))        # 将path分割成目录和文件名二元组返回， ('E:\\', 'a.txt')
print(os.path.dirname('E:\\a.txt'))      # 返回path的目录。其实就是os.path.split(path)的第一个元素, E:\
print(os.path.basename('E:\\a\\b.txt'))  # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。
# 即os.path.split(path)的第二个元素 b.txt

print(os.path.exists('E:\\a.txt'))     # 如果path存在，返回True；如果path不存在，返回False
print(os.path.isabs('E:\\day'))        # 不管存在与否
print(os.path.isfile('E:\\Asset.vsdx'))    # 如果path是一个存在的文件，返回True。否则返回False
print(os.path.isdir('E:\\'))                # 如果path是一个存在的目录，则返回True。否则返回False

print(os.path.join('b', 'E:\\', 'a',))          # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略， E:\a
print(os.path.getsize('E:\\Asset.vsdx'))       # 返回path的大小, 单位 Bytes


"""
os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间

在Linux和Mac平台上，该函数会原样返回path，在windows平台上会将路径中所有字符转换为小写，并将所有斜杠转换为饭斜杠。
>>> os.path.normcase('c:/windows\\system32\\')
'c:\\windows\\system32\\'

规范化路径，如..和/
>>> os.path.normpath('c://windows\\System32\\../Temp/')
'c:\\windows\\Temp'

>>> a='/Users/jieli/test1/\\\a1/\\\\aa.py/../..'
>>> print(os.path.normpath(a))
/Users/jieli/test1

"""



# Python 处理方式
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

# OpenStack处理方式
BASE_DIR = os.path.normpath(os.path.join(__file__, os.pardir, os.pardir))
print(BASE_DIR)
