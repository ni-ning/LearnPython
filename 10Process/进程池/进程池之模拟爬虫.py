#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from multiprocessing import Pool
import time
import random
import os


def get_page(url):
    print('正在爬取网页: %s' % url)
    time.sleep(random.randint(1, 3))
    return {'url': url}


def parse_page(page_content):
    print('正在解析网页：%s' % page_content)
    time.sleep(1)
    page_content['url'] = os.getpid()

    print('解析网页的结果为：%s' % page_content)
    # 除了打印，还可以open(), db操作

if __name__ == '__main__':
    pool = Pool()
    res_l = []
    urls = [
        'http://www.baidu.com',
        'http://linda.com',
        'http://jonathan.com'
    ]
    for url in urls:
        # get_page的返回值，传给callback函数
        res = pool.apply_async(get_page, args=(url,), callback=parse_page)
        res_l.append(res)

    # 最后res.get()展现最后效果
    for res in res_l:
        res.get()
