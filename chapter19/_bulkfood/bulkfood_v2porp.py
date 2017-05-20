#! /usr/bin/env python3
#coding=utf-8


def quantity(storage_name):
    
    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')
    return property(qty_getter, qty_setter)

class LineItem:
    ''' item '''
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


    # 构建property 对象，然后赋值给公开的类属性。
    weight = property(get_weight, set_weight)
