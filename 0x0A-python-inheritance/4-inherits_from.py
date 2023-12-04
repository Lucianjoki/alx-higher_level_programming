#!/usr/bin/python3
"""Define an inheritedclass-checking function."""


def inherits_from(obj, a_class):
    """checks if an object is an inherited instance of a class.

    Args:
        obj (any): object to check
        a_class (type): class to match type of obj to

    Returns:
        True - if obj is an inherited instance of a_class
        Otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
