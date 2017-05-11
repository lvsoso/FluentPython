# -*- coding: utf-8 -*-
"""
Created on Wed May 10 19:18:17 2017




"""

import functools32


from _clockdeco import clock


@functools32.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    print(fibonacci(6))