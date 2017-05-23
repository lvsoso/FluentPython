# -*- coding: utf-8 -*-
"""
Created on Sun May 14 22:10:04 2017

"""

from functools import wraps

def coroutine(func):
    """装饰器：向前执行到第一个`yield`表达式，预激`func`"""
    @wraps(func)
    def primer(*args,**kwargs):
        gen = func(*args,**kwargs)
        next(gen) #预激
        return gen
    return primer