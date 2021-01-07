#!/usr/bin/python3
'''
A function that add two numbers integers or floats
Functions:
    add_integer()
'''


def add_integer(a, b=98):
    '''
    Args:
        a: an int or float to add
        b: an int or float to add
    Returns:
        Result of the add of the arguments
    Raises:
        TypeError: if a or b aren't int or float
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
