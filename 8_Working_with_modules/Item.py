import csv


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

