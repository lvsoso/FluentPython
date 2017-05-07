# -*- coding: utf-8 -*-
"""
Created on Sun May 07 17:56:17 2017

"""


import bisect
import random

SIZE = 7

random.seed(1992)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print '%2d ->'%new_item, my_list