#!/usr/bin/python3
"""Real definition of a rectangle"""
    
class Rectangle:
    """Represent a Rectangle"""
    def __init__(self,width=0, height=0):
        """
        Create a new rectangle of width  and height .
        """
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if  not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <  0:
            raise ValueError("width must be >= 0")
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if  not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <  0:
            raise ValueError("height must be >= 0")