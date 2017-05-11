# -*- coding: utf-8 -*-
"""
Created on Wed May 10 23:15:01 2017

"""

import weakref

class Cheese(object):
    
    def __init__(self, kind):
        self.kind = kind
        
    def __repr__(self):
        return 'Cheese(%r)' % self.kind
    
    
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), \
           Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese
    
print sorted(stock.keys())

#['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']

del catalog

print sorted(stock.keys()) #['Parmesan'] 它是for循环最后一个引用的