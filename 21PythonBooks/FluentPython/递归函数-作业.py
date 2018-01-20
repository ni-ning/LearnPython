#!/usr/bin/env python
# -*- coding:utf-8 -*-
menus = [
    {
        'text': '北京',
        'children': [
            {'text': '朝阳', 'children': []},
            {'text': '昌平', 'children': [
                {'text': '沙河', 'children': [
                    {'text': '老男孩大厦', 'children': []},
                ]},
                {'text': '回龙观', 'children': [
                    {'text': '西三旗', 'children': []},
                ]},
                {'text': '中关村', 'children': []},
            ]},
        ]
    },
    {
        'text': '上海',
        'children': [
            {'text': '宝山', 'children': [
                # {'text': '浦东', 'children': []},
            ]},
            {'text': '金山', 'children': []},
        ]
    }
]
# menus=[{'children': [{'children': [], 'text': '沙河'}, {'children': [], 'text': '回龙观'}], 'text': '昌平'}]
# menus=[{'text': '沙河', 'children': []}, {'text': '回龙观', 'children': []}]
#深度查询
#1. 打印所有的节点
#2. 输入一个节点名字，沙河， 你要遍历找，找到了，就打印它，并返回true,false
# def get_info():

def get02(temp):

    for i in temp:
        print(i['text'])
        # print('----1>',i)
        for i2 in i['children']:
            if len(i2['children']) > 0:
                # print(len(i2['text']))
                print(i2['text'])
                temp=i2['children']
                # print('----2>',temp)

            elif len(i2['text'])>0:             #把children为空的也打印出来


                    print(i2['text'])
            #
    else:
        if len(i['children'])>0  :              #设置递归的结束条件
            # print('----3>', i['children'])

            return get02(temp)                  #递归下去，把新的temp给函数


get02(menus)


def dic(menus, location):
    for item in menus:
        if item['text'] == location:
            print(location)
    for item in menus:
        if len(item['children']) > 0:
            menus = item['children']
            dic(menus, location)

location = input('请输入地名： ')
dic(menus, location)