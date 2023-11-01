#!/usr/bin/python3
"""Print alphabet in lowercase, not followed by a new line"""
for letter in range(97, 123):
    if chr(letter) not in 'eq':
        print("{}" .format(chr(letter)), end="")
