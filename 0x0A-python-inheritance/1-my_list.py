#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """implements sorted printing for built in list class."""

    def print_sorted(self):
        """print a list in asorted ascending order."""
        print(sorted(self))
