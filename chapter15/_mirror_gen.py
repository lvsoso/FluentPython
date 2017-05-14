# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:12:49 2017

"""

import contextlib

def looking_glass():
    import sys
    original_write = sys.stdout.write
    
    def reverse_write(text):
        original_write(text[::-1])
    
    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write
    