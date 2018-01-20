#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import collections
from random import choice

# nametuple用来构建只有少数属性但是没有方法的对象
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    # __getitem__把[]操作交给了self.__cards列表，所以可以切片
    # __getitem__把数据传递过来，具体实现，自己定义
    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print("len(deck): ", len(deck))  # __len__
print("deck[0]: ", deck[0])    # [] --> __getitem__, list切片
print("deck[0:2]: ", deck[0:2])  # [] --> __getitem__, list切片
print("choice(deck): ", choice(deck))  # 标准库是语言的一部分，不用重复造轮子

# 集合类型，没有实现__contains__方法，那么in运算符就会按顺序做一次迭代搜索
# for card in reversed(deck):
#     print(card)

# 黑桃最大，红桃次之，方块再次，梅花最小
# 梅花2的大小是0，黑桃A是51
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)

