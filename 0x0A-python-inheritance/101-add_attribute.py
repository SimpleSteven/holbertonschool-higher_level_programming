#!/usr/bin/python3
'''Create a function to add a new attribute to a class'''


def add_attribute(a_class, name, value):
    '''Create a function that add a new attribute to a class. If fail,
    raise an error with a customized message.'''

    try:
        setattr(a_class, name, value)
    except AttributeError:
        raise TypeError("can't add new attribute")
