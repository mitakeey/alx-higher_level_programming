#!/usr/bin/python3
"""
This module implements  a function;returns True in even that the object is an instance of a class inherited from specified class
"""


def inherits_from(obj, a_class) -> bool:
    """implementation
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
