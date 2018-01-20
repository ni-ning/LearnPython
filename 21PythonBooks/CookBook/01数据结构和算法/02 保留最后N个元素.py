#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
保留最后N个元素
"""

from collections import deque

li = deque(maxlen=3)

li.append(0)
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)
li.append(6)
print(li)
li.appendleft('dadada')
print(li)
li.popleft()
print(li)


from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# 匹配行以及前2行
with open('words', 'r') as f:
    for line, prevlines in search(f, 'purr', 2):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-' * 20)

