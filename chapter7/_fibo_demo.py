# -*- coding: utf-8 -*-
"""
Created on Wed May 10 19:14:38 2017

"""

from _clockdeco import clock

@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    print(fibonacci(30))