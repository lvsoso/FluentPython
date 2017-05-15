# -*- coding: utf-8 -*-
"""
Created on Sun May 14 21:53:13 2017

"""

#python -m doctest -v xxx.py

def averager():
    """
    >>> coro_avg = averager()
    >>> next(coro_avg)
    >>> coro_avg.send(10)
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0
    """
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total//count
        