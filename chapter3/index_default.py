# -*- coding: utf-8 -*-
"""
Created on Tue May 09 19:11:02 2017

"""

import sys
import re
import collections


WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)

#with open("1.txt", encoding='utf-8') as fp:
with open("1.txt") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            
            index[word].append(location)
            
for word in sorted(index, key=str.upper):
    print word, index[word]