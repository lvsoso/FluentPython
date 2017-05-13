# -*- coding: utf-8 -*-
"""
Created on Sat May 13 09:30:10 2017

"""

import re
#import reprlib

RE_WORD = re.compile("\w+")


class Sentence(object):
    
    def __init__(self, text):
        """ 初始化 """
        self.text = text
        self.words = RE_WORD.findall(text)
    
    #def __getitem__(self, index):
        #return self.words[index]
    
    #实现 序列 协议
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        #return 'Sentence(%s)'%reprlib.repr(self.text)
        return 'Sentence(%s)'%(repr(self.text))
    
    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator(object):
    
    def __init__(self, words):
        self.wordsr = words
        self.index = 0
        
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word
    
    def __iter__(self):
        return self
    
if __name__ == "__main__":
    s  =Sentence("Hello Hi Morning, 'xx' !")
    print s
    for word in s:
        print word
        
    print list(s)