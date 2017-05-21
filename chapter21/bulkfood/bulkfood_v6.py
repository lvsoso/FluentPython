#coding=utf-8
import model_v6 as model

@model.entity
class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
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
    