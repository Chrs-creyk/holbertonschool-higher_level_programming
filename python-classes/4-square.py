#!/usr/bin/python3
"""empty class Square that defines a square"""


class Square:
    """private atribute of an estance"""

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
    

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size
