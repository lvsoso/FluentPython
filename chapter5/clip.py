# -*- coding: utf-8 -*-
"""
Created on Tue May 09 21:25:09 2017

"""


def clip(text, max_len=80):
    """
    在 指定出前或后 第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
        if end is None:
            end = len(text)
        
        return text[:end].rstrip()
        