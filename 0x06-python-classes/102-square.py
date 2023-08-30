#!/usr/bin/python3
"""
Module: square
"""

class Square:
    """
    Represents a square.

    Attributes:
        __size (float or int): The size of the square.

    Methods:
        __init__ : Initializes a new Square instance with an optional size.
        area(self): Returns the current square area.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with an optional size.

        Args:
            size (float or int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two Square instances have equal areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
        True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two Square instances have unequal areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
        True if the areas are unequal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks if the area of this Square instance is less than the area of another Square.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
        True if this area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the area of this Square instance is less than or equal to the area of another Square.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
        True if this area is less or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks if the area of this Square instance is greater than the area of another Square.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
        True if this area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the area of this Square instance is greater than or equal to the area of another Square.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
        True if this area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()
i
