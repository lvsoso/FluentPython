# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:16:16 2017

"""

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
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


    
def fidelity_promo(order): # 具体策略 1
    """ 积分1000 及以上 5%"""
    
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order): # 具体策略 2
    """ 单个商品为20个或以上 10%"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount
    
    
def large_order_promo(order): # 具体策略 3
    """ 不同商品数量达到 10 个 或 以上 7%"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0
    
promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order):
    """选择折扣最大的"""
    return max(promo(order) for promo in promos)
    
if __name__ == "__main__":
    hah = Customer('haha xixi', 0)
    xix = Customer('xixi', 1300)
    cart = [LineItem('banana', 4, .5),LineItem('apple', 10, 1.5),LineItem('watermellon', 5, 5.0)]
    banana_cart = [LineItem('banana', 30, .5),LineItem('apple', 10, 1.5)]
    print Order(hah, cart, fidelity_promo)
    print Order(hah, banana_cart, bulk_item_promo)
    print Order(hah, banana_cart, best_promo)
    print Order(xix, cart, best_promo)