# -*- coding: utf-8 -*-
"""
Created on Sun May 14 22:11:56 2017
"""
from coroutil import coroutine


@coroutine
def averager():
    """
    >>> coro_avg = averager()
   
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
        