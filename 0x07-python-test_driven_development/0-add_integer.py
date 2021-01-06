#!/bin/usr/python3
'''A function that add two numbers integers or floats'''


def add_integer(a, b=98):
    ''' Receive as parameters, two numbers, the second
    is optional. If the second is not given, will be replaced
    by a 98. Then add the two numbers and cast it to integers'''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
