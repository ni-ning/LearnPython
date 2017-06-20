#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# f = open('log', 'r', encoding='utf-8')
# f = open('log', 'r')
f = open('log', 'rb')
data = f.read()
f.close()

print(data)




