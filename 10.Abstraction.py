import csv

"""
Abstraction Shows the necessary attributes and hides the unnecessary properties from users
"""

"""Abstraction is a core concept in object-oriented programming (OOP), including in Python. It involves hiding the 
complex implementation details and showing only the essential features of an object. This helps in reducing 
programming complexity and effort.

In Python, abstraction is typically achieved using abstract classes and methods. An abstract class is a class that 
cannot be instantiated and often includes one or more abstract methods. These methods are declared but contain no 
implementation. Subclasses of the abstract class are expected to provide implementations for these abstract methods."""


"""
Example of Abstraction in Python
Here’s a simple example to illustrate abstraction using the abc module in Python:

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow

"""

"""
In this example:

Animal is an abstract class with an abstract method sound().
Dog and Cat are subclasses of Animal and provide their own implementations of the sound() method.
Benefits of Abstraction
# Simplifies Code: By hiding complex details, abstraction makes the code easier to understand and maintain.
# Enhances Reusability: Abstract classes can be reused across different programs.
# Improves Flexibility: Changes in the abstract class do not affect the subclasses, as long as the interface remains consistent.
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

    # Abstraction...........

    # with the __ before the connect like this __connect; it makes it a Private method
    # Which can't be accessed outside the main class
    def __connect(self, server_url):
        pass

    def __prepare_body(self):
        return f"Hello Someone; We have {self.name} {self.quantity} times; Regards, appleShop"

    def __send(self):
        pass

    def send_email(self):
        # Hiding or Abstracting to connect, prepare_body and send
        self.__connect('')
        self.__prepare_body()
        self.__send()


item_1 = Item('New Item', 400, 5)

print(item_1.price)
item_1.send_email()
