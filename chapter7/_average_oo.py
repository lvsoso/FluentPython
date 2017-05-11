# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:20:26 2017

"""

class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

