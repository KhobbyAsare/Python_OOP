# when to use class method and when to use static method

"""
Class Method

A class method is a method that is bound to the class and not the instance of the class. It can modify the class
state that applies across all instances of the class. Class methods are defined using the @classmethod decorator and
take cls as the first parameter, which refers to the class itself.

When to use:

When you need to access or modify the class state.
When you need to create factory methods that return an instance of the class.
Example:
"""


class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.instance_variable = value

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1
        return cls.class_variable


# Usage
print(MyClass.class_variable)  # Output: 0
MyClass.increment_class_variable()
print(MyClass.class_variable)  # Output: 1

"""
Static Method
A static method is a method that does not modify the class or instance state. It is defined using the @staticmethod decorator and does not take self or cls as the first parameter. Static methods are used to perform utility functions that are related to the class but do not need to access or modify the class or instance state.

When to use:

When you need a utility function that does not access or modify the class or instance state.
When the method logically belongs to the class but does not need to interact with the class or instance variables.
Example:
"""


class MyClass:
    @staticmethod
    def utility_function(x, y):
        return x + y


# Usage
result = MyClass.utility_function(5, 3)
print(result)  # Output: 8

"""
Summary
Class Method: Use when you need to access or modify the class state.
Static Method: Use when you need a utility function that does not interact with the class or instance state.
"""
