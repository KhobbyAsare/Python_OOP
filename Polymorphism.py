"""
It is referring to use of single type of entity to represent different types of object in different scenarios

poly = many
morphism = forms
"""

"""
Polymorphism is another key concept in object-oriented programming (OOP), including in Python. It allows objects of
different classes to be treated as objects of a common superclass. Essentially, polymorphism means “many forms,
” and it enables a single function or method to work in different ways depending on the object it is acting upon.

Here are a few ways polymorphism can be implemented in Python:
"""

# 1. Function Polymorphism
# A single function can operate on different types of objects. For example, the built-in
# len() function can be used with strings, lists, tuples, etc.

print(len("Hello"))  # Output: 5
print(len([1, 2, 3, 4]))  # Output: 4
print(len((10, 20, 30)))  # Output: 3


# 2. Class Polymorphism
# Different classes can have methods with the same name, and we can call these methods on
# objects of different classes in a uniform way.


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: int | float, quantity: int | float = 1):
        assert price >= 0, f"Price {price} is not greater than Zero"
        assert quantity >= 0, f"Price {quantity} is not greater than Zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return f"${self.price * self.quantity}"

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        # {self.__class__.__name__}:  for getting the name of that particular class
        return f"{self.__class__.__name__}('{self.name}', '{self.price}','{self.quantity}')"

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


item_1 = Item('GOOD', 100, 40)
item_2 = Item('BETTER', 200, 50)

# add_discount can be used in many different forms on the instance class create
item_1.apply_discount()
item_2.apply_discount()


