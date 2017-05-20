#coding=utf-8
import model_v5 as model

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
    print(LineItem.price)
    br_nuts = LineItem("Brazil nuts", 10, 34.95)
    print(br_nuts.price)
    