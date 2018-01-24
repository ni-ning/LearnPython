#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from multiprocessing import Pool


def work(n):
    return n ** 2

if __name__ == '__main__':
    pool = Pool(6)
    res_l = []
    for i in range(6):
        res = pool.apply_async(work, args=(i, ))
        res_l.append(res)

    for item in res_l:
        print(item.get())  # 取得异步执行的结果
    """
    应用场景：爬虫，线程池去爬网页，爬下来的内容交给回调函数去分析处理
    """
