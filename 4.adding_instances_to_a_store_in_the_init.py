class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: int | float, quality: int | float = 1):

        assert price >= 0, f"Price {price} is not greater than Zero"
        assert quality >= 0, f"Price {quality} is not greater than Zero"

        self.name = name
        self.price = price
        self.quality = quality

        # actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return f"${self.price * self.quality}"

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # Representing the store well like the way it was created
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}','{self.quality}')"


item1 = Item('Hilary', 200.342, 4)
item2 = Item('Iphone 13', 4000, 2)
item3 = Item('laptop', 1000, 3)
item4 = Item('Mouse', 30, 2)
item5 = Item('Keyboard', 200, 2)


print(Item.all)
print(len(Item.all))

for instance in Item.all:
    print(instance.name)
