#!/usr/bin/python3
"""
Defines an empty class Rectangle.
"""


class Rectangle:
    """
    Represents a Rectangle with validated width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.
        Args:
            width (int): The width of the rectangle (default: 0).
            height (int): The height of the rectangle (default: 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width attribute.
        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        Validates that width is a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        Validates that height is a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle.
        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        using the '#' character.
        If the width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join(
                [str(self.print_symbol) *
                 self.__width for _ in range(self.__height)]
            )

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        that can be used to recreate a new instance with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"
