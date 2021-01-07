#!/usr/bin/python3
'''
    A function that print the first
    and last name passed as string parameters
    Functions:
        matrix_divided()
'''


def say_my_name(first_name, last_name=""):
    '''
    Args:
        first_name: a string name
        last_name: a string last name
    Raises:
        TypeError:
        if first_name or last_name aren't strings
    '''

    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    elif type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
