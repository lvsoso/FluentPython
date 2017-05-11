# -*- coding: utf-8 -*-
"""
Created on Wed May 10 11:21:41 2017

"""
#from abc import ABC, abstractmethod #python3

from abc import abstractmethod
from collections import namedtuple

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
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

class Promotion(): #策略抽象类
    
    @abstractmethod
    def discount(self, order):
        """返回折扣金额（正值）"""
        pass
    
class FidelityPromo(Promotion): # 具体策略 1
    """ 积分1000 及以上 5%"""
    
    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion): # 具体策略 2
    """ 单个商品为20个或以上 10%"""
    
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount
    
class LargeOrderPromo(Promotion): # 具体策略 3
    """ 不同商品数量达到 10 个 或 以上 7%"""
    
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0
    
if __name__ == "__main__":
    hah = Customer('haha xixi', 0)
    xix = Customer('xixi', 1300)
    cart = [LineItem('banana', 4, .5),LineItem('apple', 10, 1.5),LineItem('watermellon', 5, 5.0)]
    banana_cart = [LineItem('banana', 30, .5),LineItem('apple', 10, 1.5)]
    print Order(hah, cart, FidelityPromo())
    print Order(hah, banana_cart, BulkItemPromo())