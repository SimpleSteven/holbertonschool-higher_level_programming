#!/bin/usr/python3
'''A function that add two numbers integers or floats'''


def add_integer(a, b=98):
    '''
    Args: a, b = int or float
    Raise error if the args aren't int float
    Cast a and b to int
    Add a + b and return it
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
