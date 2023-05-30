#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square.
        Args:
        size(int):the size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #."""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
