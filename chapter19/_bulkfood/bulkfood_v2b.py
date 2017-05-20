#! /usr/bin/env python3
#coding=utf-8

class LineItem:
    ''' item '''
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def get_weight(self):
        return self.__weight
    
    def set_weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError("value must be > 0")

    # 构建property 对象，然后赋值给公开的类属性。
    weight = property(get_weight, set_weight)
