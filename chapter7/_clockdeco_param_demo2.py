# -*- coding: utf-8 -*-
"""
Created on Wed May 10 20:55:58 2017

"""

import time
from _clockdeco_param import clock

@clock('{name}({args}) dt={elapsed:0.3f}s')
def snooze(seconds):
    time.sleep(seconds)

for i in range(3):
    snooze(.123)