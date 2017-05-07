#coding=utf-8

"""
    用python表示扑克牌
"""

import collections

Card = collections.namedtuple("Card", ["rank", 'suit'])

class FrenchDeck(object):
    """
    用python表示扑克牌
    1. 通过实现 __len__ 和 __getitem__ 这两个特殊方法, 能近似序列数据类型进行操作
    2. 对于Python内置类型， __len__ CPython 直接找 PyVarObject 的 ob_size
       PyVarObject 是表示内存中长度可变的内置对象的 C 语言结构体。
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hears'.split()


    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == "__main__":
    deck = FrenchDeck()
    print len(deck)
    print deck[0]
    print deck[-1]
    from random import choice
    print choice(deck)
    print deck[:3]
    print deck[12::13]

    #实现了 __getitem__方法
    for card in deck:
        print card
    #可反向迭代
    for card in reversed(deck):
        print card
    
    Card("Q", "hearts") in deck