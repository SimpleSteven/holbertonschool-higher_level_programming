#!/bin/usr/python3
'''
    A function that print square with
    the character #
    Functions:
        print_square(size)
'''


def print_square(size):
    '''
    Args:
        size: an integer to print a square
        of the character #
    Raises:
        TypeError:
        If size isn't an integer, or if it isn't
        an integer and is less than 0
        ValueError:
        If size is less than 0
    '''

    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)
