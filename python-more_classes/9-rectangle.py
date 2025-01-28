#!/usr/bin/python3
"""
Defines a class Rectangle.
"""


class Rectangle:
    """
    Represents a Rectangle with validated width and height.
    Tracks the number of instances created and deleted.
    Supports customizable string representation symbol.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.
        Increments the class attribute number_of_instances.
        Args:
            width (int): The width of the rectangle (default: 0).
            height (int): The height of the rectangle (default: 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        Args:
            value (int): The new width of the rectangle.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
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
        Args:
            value (int): The new height of the rectangle.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
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
        return 2 * (self.__width + self.__height)

    @classmethod
    def square(cls, size=0):
        """
        Creates a new Rectangle instance with width and height equal to size.

        Args:
            size (int): The size of the square (default: 0).

        Returns:
            Rectangle: A new Rectangle instance with width == height == size.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        # Utilise cls pour créer une nouvelle instance
        return cls(size, size)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        using the `print_symbol`.
        If the width or height is 0, returns an empty string.
        Returns:
            str: A visual representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        # Use print_symbol to represent the rectangle
            return "\n".join(
                [str(self.print_symbol) *
                 self.__width for _ in range(self.__height)]
            )

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        that can be used to recreate a new instance with eval().
        Returns:
            str: A string in the format 'Rectangle(width, height)'.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        Decrements the class attribute number_of_instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the larger area.
        If both have the same area, returns rect_1.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the larger area
            or rect_1 if both are equal.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
