#coding=utf-8


#特性工厂函数与描述符类比较
def quantity():
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0

    storage_name = '_{}:{}'.format("quantity", quantity.counter)

    def qty_getter(instance):
        return getattr(instance, storage_name)
    
    def qty_setter(instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')
    
    return property(qty_getter, qty_setter)

class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

if __name__ == "__main__":
    print(LineItem.price)
    br_nuts = LineItem("Brazil nuts", 10, 34.95)
    print(br_nuts.price)
    