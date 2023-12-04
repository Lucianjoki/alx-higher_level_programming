#!/usr/bin/python3
"""Defines a class and inherited class functions."""


def is_kind_of_class(obj, a_class):
    """check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): oject to check.
        a_class (type): class to match the type of obj to.
    Returns:
        True - if obj is an instance or inherited instance of a_class
        Otherwise - False
    """

    if isinstance(obj, a_class):
        return True
    return False
