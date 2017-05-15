# -*- coding: utf-8 -*-
"""
Created on Sun May 14 20:33:53 2017

"""
#from inspect import getgeneratorstate


def simple_coroutine():
    print '-> coroutine started'
    x = yield
    print '-> coroutine receviedL', x
    
my_coro = simple_coroutine()

"""
my_coro
Out[12]: <generator object simple_coroutine at 0x0BD58760>

next(my_coro)
-> coroutine started

my_coro.send(42)
-> coroutine receviedL 42
Traceback (most recent call last):

  File "<ipython-input-14-6eb1f5a64a1d>", line 1, in <module>
    my_coro.send(42)

StopIteration


"""

def simple_coroutine2():
    print '-> coroutine started'
    x = yield
    print '-> coroutine receviedL', x
    
my_coro2 = simple_coroutine2()
print getgeneratorstate(my_coro2)
my_coro2.send(28)
my_coro2.send(77)
print getgeneratorstate(my_coro2)
