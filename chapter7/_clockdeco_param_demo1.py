# -*- coding: utf-8 -*-
"""
Created on Wed May 10 20:54:07 2017

"""

import time
from _clockdeco_param import clock


@clock('{name}: {elapsed}s')
def snooze(seconds):
    time.sleep(seconds)

for i in range(3):
    snooze(.123)