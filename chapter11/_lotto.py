# -*- coding: utf-8 -*-
"""
Created on Fri May 12 13:11:45 2017

"""

import random

from _tombola import Tombola

class LotteryBlower(Tombola):
    
    def __init__(self, iterable):
        self._balls = list(iterable)
    
    def load(self, items):
        self._balls.extend(items)
        
    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)
        
    def loaded(self):
        return bool(self._balls)
    
    def inspect(self):
        return tuple(sorted(self._balls))