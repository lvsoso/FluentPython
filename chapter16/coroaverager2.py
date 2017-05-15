# -*- coding: utf-8 -*-
"""
Created on Sun May 14 22:22:13 2017

"""

from collections import namedtuple


Result = namedtuple('Result', 'count average')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        print term
        if term is None:
            break
        total += term
        count += 1
        average = total//count
    return Result(count, average)