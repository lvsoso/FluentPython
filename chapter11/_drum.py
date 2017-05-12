# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:27:20 2017

"""

from random import shuffle

from _tombola import Tombola

class TumblingDrum(Tombola):
    
    def __init__(self, iterable):
        self._balls = []
        self.load(iterable)
    
    def load(self, iterable):
        self._balls.extend(iterable)
        shuffle(self._balls)
        
    def pick(self):
        return self._balls.pop()
    