# -*- coding: utf-8 -*-
"""
Created on Tue May 09 19:13:40 2017

"""


class StrKeyDict0(dict):
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
                    
    def get(self, key, default=None):
        try:
            return self[key] #键不存在会去调用 __missing__
        except KeyError:
            return default
        
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
        