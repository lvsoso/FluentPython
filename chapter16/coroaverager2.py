# -*- coding: utf-8 -*-
"""
Created on Sun May 14 22:22:13 2017

"""

def chain(*iterables):
    for it in iterables:
        yield from it
s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))


from collections import namedtuple


Result = namedtuple('Result', 'count average')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        print(term)
        if term is None:
            break
        total += term
        count += 1
        average = total//count
    return Result(count, average)

if __name__ == "__main__":
    coro_avg = averager()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(6.5)
    try:
        coro_avg.send(None)
    except Exception as  e:
        result = e.value
    print(result)
    #Result(count=3, average=15.0)

    """
    Traceback (most recent call last):
  File "f:\Pcode\FluentPython\chapter16\coroaverager2.py", line 32, in <module>
    coro_avg.send(None)
StopIteration: Result(count=3, average=15.0)
    """