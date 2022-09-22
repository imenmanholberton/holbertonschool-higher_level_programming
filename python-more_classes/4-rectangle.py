#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle():
    """Represent a Rectangle"""
    def __init__(self, width=0, height=0):
        """
        Create a new rectangle of width  and height.
        Args:
            width (int): The width of a new rectangle:
            height (int): The height of the new rectangle:
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """print rectangle"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return (string)
        for i in range(self.__height):
            for j in range(self.__width):
                string = string + "#"
            string = string + "\n"
        return string[0:-1]
    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)