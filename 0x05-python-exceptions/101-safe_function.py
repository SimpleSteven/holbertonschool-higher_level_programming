#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        a = fct(*args)
    except (ZeroDivisionError, IndexError) as error:
        sys.stderr.write("Exception: " + str(error))
        return None
    return a
