# -*- coding: utf-8 -*-
"""
Created on Fri May 12 13:55:47 2017

"""

from random import randrange

from _tombola import Tombola


#把Tombolist 注册为Tombola 的虚拟子类。 python3
#@Tombola.register
class TomboList(list):
    
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TombolList')
        
    load = list.extend
    
    def loaded(self):
        return bool(self)
    
    def inspect(self):
        return tuple(sorted(self))

Tombola.register(TomboList)


if __name__ == "__main__":
    print issubclass(TomboList, Tombola)
    print TomboList.__mro__