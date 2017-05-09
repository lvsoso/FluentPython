# -*- coding: utf-8 -*-
"""
Created on Tue May 09 19:20:27 2017


"""

import collections


class StrkeyDict(collections.UserDict):
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
                    
    def __contains__(self, key):
        return str(key) in self.data

    def __set__setitem__(self, key, item):
        self.data[str(key)] = item