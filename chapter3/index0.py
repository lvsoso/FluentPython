# -*- coding: utf-8 -*-
"""
Created on Tue May 09 19:04:05 2017

"""

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
#with open("1.txt", encoding='utf-8') as fp:
with open("1.txt") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            
            #1
            #occurrences = index.get(word, [])
            #occurrences.append(location)
            #index[word] = occurrences

            #2
            index.setdefault(word, []).append(location)
            
for word in sorted(index, key=str.upper):
    print word, index[word]