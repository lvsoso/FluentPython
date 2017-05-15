# -*- coding: utf-8 -*-
"""
Created on Sun May 14 20:27:32 2017

"""

from collections import abc
from osconfeed import load
import keyword

class FrozenJSON:
    """
        只读接口，使用属性表示法访问JSON类对象
    """

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


if __name__ == "__main__":
    raw_feed = load()
    feed = FrozenJSON(raw_feed)    
    print(len(feed.Schedule.speakers))
    print(sorted(feed.Schedule.keys()))
    for key, value in sorted(feed.Schedule.items()):
        print('{:3} {}'.format(len(value), key))
        
    talk = feed.Schedule.events[40]
    print(talk.name)
    print(talk.a)
    print("===============")
    grad = FrozenJSON({'name': 'Jim Bo', 'class': 1982})
    print(getattr(grad, 'class'))
    #print(grad.class)
    