import csv

"""Encapsulation is a fundamental concept in object-oriented programming (OOP), including in Python. It refers to the 
bundling of data (attributes) and methods (functions) that operate on the data into a single unit, typically a class. 
This helps in restricting direct access to some of an object’s components, which can prevent the accidental 
modification of data.

In Python, encapsulation is achieved using access modifiers:

Public members: Accessible from anywhere outside the class.
Protected members: Accessible within the class and its subclasses. These are prefixed with a single underscore (_).
Private members: Accessible only within the class. These are prefixed with double underscores (__).
"""


"""
# Encapsulation restrict users from directly accessing and modifying data,
# So they have the opportunity to give it a value at the initialization level and after that they can't modify it
"""


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: int | float, quantity: int | float = 1):
        assert price >= 0, f"Price {price} is not greater than Zero"
        assert quantity >= 0, f"Price {quantity} is not greater than Zero"

        # changing name to read_only using the single underscore
        self._name = name
        # __price is now a Read_Only Property
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return f"${self.__price * self.quantity}"

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def __repr__(self):
        # {self.__class__.__name__}:  for getting the name of that particular class
        return f"{self.__class__.__name__}('{self.name}', '{self.price}','{self.quantity}')"

    # create a class method for the instantiation
    @classmethod  # class method decorator
    def instantiate_from_csv(cls):
        # Reading from the csv file
        """
        r = read
        w = write

        """
        with open('5.items.csv', 'r') as f:
            reader = csv.DictReader(f)  # DictReader(f) will read the items like a dictionary
            items = list(reader)  # convert the reader which is in a dictionary format into a list items

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),

            )

    @staticmethod
    def is_integer(number):
        # we will count out the float that are point zero
        # for e.g: 5.0, 10.0
        if isinstance(number, float):
            # count out te float that are point zero
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False

    # read-only name
    @property
    def name(self):
        return self._name

    # Being able to set or change the value of a read-only
    @name.setter
    def name(self, value):
        # you can check something before changing the value
        if len(value) > 10:
            raise Exception('Name is too long')
        else:
            self._name = value

    # Read-only price
    @property
    def price(self):
        return self.__price

    # Creating a read_only attribute using the decorator property
    @property
    def name_readOnly(self):
        return 'Read Only Name'


item_1 = Item('New Item', 400, 5)

print(item_1.name_readOnly)
print(item_1.price)
item_1.price = 890
item_1.name = "more"
print(item_1.name)


