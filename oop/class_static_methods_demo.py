# class_static_methods_demo.py

class Calculator:
    """
    Demonstrate @staticmethod and @classmethod.
    - calculation_type is a class attribute.
    - add is a static method (no access to cls or self).
    - multiply is a class method (receives cls and can access class attributes).
    """
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Print the class attribute 'calculation_type' and return the product.
        Demonstrates that class methods receive the class as the first argument.
        """
        print("Calculation type: {}".format(cls.calculation_type))
        return a * b
