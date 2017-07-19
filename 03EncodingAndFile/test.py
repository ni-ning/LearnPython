#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

f = open('test.txt', 'r', encoding='utf-8')
while True:
    inp = input('q to exit or go on:>  ')
    if inp.strip() == 'q':
        f.close()
        break
    else:
        for i in range(0, 3):
            line = f.readline()
            if line:
                print(line, end='')
            else:
                f.close()
                exit()



