#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
一 什么是正则
正则就是用一些具有特殊含义的的符号组合到一起(称为正则表达式)来描述字符或字符串的方法
或者说：正则就是用来描述一类事物的规则
(在Python中)它内嵌在Python中，并通过re模块实现
正则表达式模式被编译成一系列的字节码，然后由用 C 编写的匹配引擎执行

在线匹配工具  http://tool.oschina.net/regex/
"""

import re
s = """
http://www.baidu.com
1011010101
xxxx@126.com
你好
21213
010-3141
linda@gmail.com
"""
res = re.findall(r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?", s)
print(res)  # ['xxxx@126.com', 'linda@gmail.com']

"""
二 常用匹配模式(元字符)
http://blog.csdn.net/yufenghyc/article/details/51078107
"""

# \w匹配字母数字及下划线
# \W匹配非字母数字及下划线
print(re.findall('\w', 'as123df_*|'))  # ['a', 's', '1', '2', '3', 'd', 'f', '_']
print(re.findall('\W', 'as123df_*|'))  # ['*', '|']
print(re.findall('a\wb', 'a_b a3b aEb a*b'))  # ['a_b', 'a3b', 'aEb']

# \s 匹配任意空白字符，等价于[\t\n\r\f]
# \S 匹配任意非空白字符
print(re.findall('\s', 'a b\n\td'))  # [' ', '\n', '\t']
print(re.findall('\S', 'a b\n\td'))  # ['a', 'b', 'd']

# \d 匹配任意数字，等价于[0-9]
# \D 匹配任意非数字
print(re.findall('\d', 'ab#*12db'))  # ['1', '2']
print(re.findall('\D', 'ab#*12db'))  # ['a', 'b', '#', '*', 'd', 'b']

# \n匹配一个换行符
# \t匹配一个制表符
print(re.findall('\n', '\ndd\n\n'))    # ['\n', '\n', '\n']
print(re.findall('\t', '\ndd\t#*&|'))  # ['\t']

# ^匹配字符串的开头
# $匹配字符串的末尾
print(re.findall('h', 'hello linda hao123'))   # ['h', 'h']
print(re.findall('^h', 'hello linda hao123'))  # ['h']
print(re.findall('^h', 'ello linda hao123'))   # []

print(re.findall('3', '3ello linda3 hao123'))     # ['3', '3', '3']
print(re.findall('3$', '3ello linda3 hao123'))    # ['3']
print(re.findall('123$', '3ello linda3 hao123'))  # ['123']
print(re.findall('3$', '3ello linda3 hao12'))     # []

# . 匹配任意一个字符, 除了换行符
print(re.findall('a.b', 'a b a*b a|b abd a\nb a\tb'))        # ['a b', 'a*b', 'a|b', 'a\tb']
print(re.findall('a.b', 'a b a*b a|b abd a\nb a\tb', re.S))  # ['a b', 'a*b', 'a|b', 'a\nb', 'a\tb']，可以匹配换行符

# [] 匹配任意一个字符，可以指定某个，或范围，特意检索-时，-需放在开头或结尾
# [^] 不在[]中的字符：[^abc]匹配除了a,b,c之外的字符
print(re.findall('a[1,2\n]b', 'a1b a2b a|b a,b a\nb a\tb'))           # ['a1b', 'a2b', 'a,b', 'a\nb']
print(re.findall('a[0-9]b', 'a1b a2b a|b a,b a\nb a\tb'))             # ['a1b', 'a2b']
print(re.findall('a[0-9a-zA-Z-]b', 'a1b a2b a|b abb a\nb aBb a-b'))  # ['a1b', 'a2b', 'abb', 'aBb', 'a-b']
print(re.findall('a[^0-9]b', 'a1b a2b a|b a,b a\nb a\tb'))           # ['a|b', 'a,b', 'a\nb', 'a\tb']

# * + ? {n, m} 表示重复
# * 匹配0个或多个的表达式
# ab*  a   ab   abbbbbb
print(re.findall('ab*', 'a'))      # ['a']
print(re.findall('ab*', 'ab'))     # ['ab']
print(re.findall('ab*', 'abbb'))   # ['abbb']
print(re.findall('ab*', 'bbb'))    # [] 需a开头

# + 匹配1个或多个的表达式
print(re.findall('ab+', 'a'))      # []  至少有一个b
print(re.findall('ab+', 'ab'))     # ['ab']
print(re.findall('ab+', 'abbb'))   # ['abbb']
print(re.findall('ab+', 'bbb'))    # []

# ab[123]      ab1  ab2  ab3
# ab[123]+    ab111...  ab222... ab333...  ab122...
print(re.findall('ab[123]+', 'ab122'))  # ['ab122']

# {2} 匹配2个表达式，明确告诉, * == {0,} + == {1,}
print(re.findall('ab{3}', 'abbb abbb abb ab'))    # ['abbb', 'abbb']
print(re.findall('ab{1,3}', 'abbb abbb abb ab'))  # ['abbb', 'abbb', 'abb', 'ab']

# ? 匹配0个或1个表达式  ab?c   ac  abc
print(re.findall('ab?c', 'ac abc aec a1c'))  # ['ac', 'abc']

# .*  任意长度的任意字符，贪婪匹配  ---直到最后一个c，对于正则而言 不友好
print(re.findall('a.*c', 'ac abc aec a1c'))  # ['ac abc aec a1c']

# .*?  任意长度的任意字符，非贪婪匹配  碰到c停， ？只是转为非贪婪匹配标识，与单独的？区分开
print(re.findall('a.*?c', 'ac abc aec a1c'))  # ['ac', 'abc', 'aec', 'a1c']

# a|b 匹配a或b
print(re.findall('compan(?:y|ies)', 'Too many companies have gone bankrupt, and the next one is my company')) # ['companies', 'company']

# ()匹配括号内的表达式，也表示一个组
print(re.findall('ab+123', 'ababab123'))      # ['ab123']
print(re.findall('(ab)+123', 'ababab123'))    # ['ab']，只是()里的值
print(re.findall('(?:ab)+123', 'ababab123'))  # ['ababab123']

# print(re.findall('a\\c','a\c')) # 对于正则来说a\\c确实可以匹配到a\c,但是在python解释器读取a\\c时，会发生转义，然后交给re去执行，所以抛出异常
print(re.findall(r'a\\c', 'a\c')) #r代表告诉解释器使用rawstring，即原生字符串，把我们正则内的所有符号都当普通字符处理，不要转义
print(re.findall('a\\\\c', 'a\c')) #同上面的意思一样，和上面的结果一样都是['a\\c']

