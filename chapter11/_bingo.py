# -*- coding: utf-8 -*-
"""
Created on Fri May 12 13:01:53 2017

"""

import random

from _tombola import Tombola

class BingoCage(Tombola):
    
    def __init__(self, items):
        self._radomizer = random.SystemRandom()
        self._items = []
        self.load(items)
    
    def load(self, items):
        self._items.extend(items)
        self._radomizer.shuffle(self._items)
        
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCase")
        
    def __call__(self):
        self.pick()