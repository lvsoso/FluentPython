# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:23:05 2017

"""


def make_averager():
    series = []
    
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    
    return averager