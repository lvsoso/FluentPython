# -*- coding: utf-8 -*-
"""
Created on Wed May 10 23:08:27 2017


"""

import time

import weakref

s1 = {1, 2, 3}
s2 = s1

def bye():
	print('Gone with the wind...')
	
ender = weakref.finalize(s1, bye)

print ender.alive
def s1

print ender.alive
s2 = 'spam'
print ender.alive