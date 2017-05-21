#coding=utf-8
import model_v8 as model


class LineItem(model.Entity):
    print("==========")
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        # 此时会先指向Entity的初始化
        print("__init__ in  lineItem")
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
    
if __name__ == "__main__":
    raisins = LineItem('Guo zi', 10, 6.95)
    print(dir(raisins))
    print(LineItem.description.storage_name)
    print(raisins.description)
    print(getattr(raisins, '_NonBlank#description'))
    print("==================")
    for name in LineItem.field_names():
        print(name)
    
    