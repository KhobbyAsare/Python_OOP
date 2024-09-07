class Item:
    # class attribute
    pay_rate = 0.8  # The pay rate after 20% discount

    def __init__(self, name: str, price: int | float, quality: int | float = 1):
        print('hello')

        assert price >= 0, f"Price {price} is not greater than Zero"
        assert quality >= 0, f"Price {quality} is not greater than Zero"

        self.name = name
        self.price = price
        self.quality = quality

    def calculate_total_price(self):
        return f"${self.price * self.quality}"

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item('Hilary', 200.342, 4)

print(item1.calculate_total_price())

"""
pay_rate is accessible on the main class and its instance
 the reason the instance is able to access the class attribute is that
when you try to access it from the instance it checks if it has that property or method
if not it move up the tree to the parent class to check, if not it will move up, till it finds it and make use of it

So item1 is getting it from its parent class
"""

print(Item.pay_rate)
print(item1.pay_rate)

print(Item.__dict__)  # show all the attribute for the class level
print(item1.__dict__)  # show all the attribute for the instance level

"""
Item class {'__module__': '__main__', 'pay_rate': 0.8, '__init__': <function Item.__init__ at 0x0000023D2D4F9DA0>, 
'calculate_total_price': <function Item.calculate_total_price at 0x0000023D2D4FA340>, '__dict__': <attribute 
'__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}

item1
{'name': 'Hilary', 'price': 200.342, 'quality': 4}
"""

item2 = Item('Iphone 13', 4000, 2)

# changing the pay_rate value for this instance
item2.pay_rate = 0.5

item2.apply_discount()
print(item2.price)
print(item1.price)
