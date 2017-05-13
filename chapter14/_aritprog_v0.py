# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:51:58 2017

"""

import itertools

class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        #先做加法运算，然后使用计算结果的类型强制转换生成的结果。
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index
        
def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index
            
def aritprog_gen_v3(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen
    
if __name__ == "__main__":
    ap = ArithmeticProgression(0, 0.5, 6)
    print list(ap)
    ag = aritprog_gen(0, 0.5, 6)
    print list(ap)