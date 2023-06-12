#!/usr/bin/python3
"""
a function that returns True if the object is exactly
an instance of the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """ Return True or False"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
