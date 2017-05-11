# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:39:45 2017

"""

from collections import namedtuple
import inspect

import promotions

Customer = namedtuple('Customer', 'name fidelity')


class LineItem(object): #商品
    
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
        
    def total(self):
        return self.price * self.quantity


class Order: #上下文
    
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
        
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())



    
promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]
         
def best_promo(order):
    """选择折扣最大的"""
    return max(promo(order) for promo in promos)
    
if __name__ == "__main__":
    hah = Customer('haha xixi', 0)
    xix = Customer('xixi', 1300)
    cart = [LineItem('banana', 4, .5),LineItem('apple', 10, 1.5),LineItem('watermellon', 5, 5.0)]
    banana_cart = [LineItem('banana', 30, .5),LineItem('apple', 10, 1.5)]
    print Order(hah, cart, promotions.fidelity_promo)
    print Order(hah, banana_cart, promotions.bulk_item_promo)
    print Order(hah, banana_cart, best_promo)
    print Order(xix, cart, best_promo)

