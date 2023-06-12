#!/usr/bin/python3
"""
Class
"""


class MyList(list):
    """Class MyList"""

    def __init__(self):
        """Inherit the mother class"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
