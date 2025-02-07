#!/usr/bin/python3
"""
Defines an abstract class Shape and its concrete subclasses Circle and Rectangle.
"""

from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    Requires implementation of area() and perimeter() in subclasses.
    """
    @abstractmethod
    def area(self):
        """Must return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Must return the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Represents a circle with a given radius.
    Implements area() and perimeter() methods.
    """

    def __init__(self, radius):
        """
        Initializes a Circle with a given radius.
        """
        self.radius = abs(radius)

    def area(self):
        """Returns the area of the circle."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Returns the perimeter (circumference) of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle with given width and height.
    Implements area() and perimeter() methods.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with given width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
