#!/usr/bin/python3

"""Defines a square"""


class Square:
    """represents a square."""

    def __init__(self, size=0):
        """initializes a new square.
        Args:
        size(int)=0: the optional size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
