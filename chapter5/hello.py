# -*- coding: utf-8 -*-
"""
Created on Tue May 09 21:23:10 2017


"""

import bobo
@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person
