#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
        size(int)=0: optional size of a new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area."""
        return(self.__size * self.__size)
