from Item import Item


# inheritance....... Parent to Child ......
class Phone(Item):
    def __init__(self, name: str, price: int | float, broken_phones: bool, quantity: int | float = 1, ):
        # call to the parent with the super to access the parents properties and assertion

        super().__init__(name, price, quantity)
        assert broken_phones == True | False, f"broken phone value must be True or False, not {broken_phones}"

        self.broken_phones = broken_phones

        Item.all.append(self)


phone1 = Phone('one', 34, True, 6)
print(phone1)
