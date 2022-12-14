#!/usr/bin/python3
"""Define a square with private instance"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """initialise  variable
        Args:
        size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """Public instance method"""
    def area(self):
        """returns the current square area"""
        return(self.__size * self.__size)
