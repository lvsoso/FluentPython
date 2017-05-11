# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:39:50 2017

"""

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