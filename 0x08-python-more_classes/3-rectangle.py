#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Creates a class of a rectangle object
    """

    def __init__(self, width=0, height=0):
        """A method to initialise the object
        Args:
            width - the width of the rectangel
            height - the height of the rectangel
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """A width getter function
        Return: the width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """A width setter function
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A height getter function
        Return: the height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """A height setter function
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A function that returns the area of
        the rectangle object
        Return: the area of the rectangle
        """

        return self.width * self.height

    def perimeter(self):
        """A function that returns the perimeter
        of the rectangle object
        Return: the perimeter of the rectangle
        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """A function that returns the rectangle
        as #

        Return: the rectangle as #
        """

        rect = ""
        if self.width == 0 or self.height == 0:
            return rect

        for i in range(self.height):
            rect += ("#" * self.width) + "\n"

        return rect[0:-1]
