# polymorphism_demo.py
import math

class Shape:
    """Base shape class. Derived classes should override area()."""
    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """Rectangle with length and width."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Return area of the rectangle (length * width)."""
        return self.length * self.width


class Circle(Shape):
    """Circle with radius."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return area of the circle (pi * r^2)."""
        return math.pi * (self.radius ** 2)

