#!/usr/bin/python3
"""
Defines Square class that inherits from Rectangle.
"""

# On importe la classe Rectangle
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a square with a given size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
