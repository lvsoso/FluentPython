# -*- coding: utf-8 -*-
"""
Created on Sat May 13 08:09:33 2017
"""

import re
#import reprlib

RE_WORD = re.compile("\w+")


class Sentence:
    
    def __init__(self, text):
        """ 初始化 """
        self.text = text
        self.words = RE_WORD.findall(text)
    
    #实现 序列 协议
    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        #return 'Sentence(%s)'%reprlib.repr(self.text)
        return 'Sentence(%s)'%(repr(self.text))

if __name__ == "__main__":
    s  =Sentence("Hello Hi Morning, 'xx' !")
    print s
    for word in s:
        print word
        
    print list(s)