#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square.
        Args:
        size(int): the size of the new square.
        position(int, int): position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of the position of the square"""
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
