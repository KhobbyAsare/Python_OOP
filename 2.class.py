class Item:
    # __init__(self) is like a constructor in JS
    def __init__(self, name: str, price: int | float, quality: int | float = 1):
        # the __init__ will call per the number of times you are instantiating the class
        # so if I create 2 instances from this class this will also call 2 times
        print('hello')

        # To check it the type we are expecting is what is passed to the init of the class
        # now we are checking if price and quantity is greater than 0
        assert price >= 0, f"Price {price} is not greater than Zero"
        assert quality >= 0, f"Price {quality} is not greater than Zero"

        self.name = name
        self.price = price
        self.quality = quality

    def calculate_total_price(self):
        return f"${self.price * self.quality}"


item1 = Item('Hilary', 200.342, 4)
item2 = Item('Mike', 300, 2)


print(item1.calculate_total_price())
print(item2.calculate_total_price())

print(item1.name)
print(item2.name)
