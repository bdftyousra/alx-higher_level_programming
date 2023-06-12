#!/usr/bin/python3
"""
A class MyInt that inherits from int:
MyInt is a rebel. MyInt has == and != operators inverted
I'm not allowed to import any module
"""


class MyInt(int):
    """
    MyInt that inherits from int
    """

    def __init__(self, num):
        """initialize num"""
        self.num = num

    def __eq__(self, other):
        """
        Return:
           True if both not equal
        """
        return self.num != other

    def __ne__(self, other):
        """
        Return:
           True if both equal
        """
        return self.num == other
