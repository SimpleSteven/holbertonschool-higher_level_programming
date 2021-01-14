#!/usr/bin/python3
"""Create a LockedClass"""


class LockedClass:
    """Class that just avoid to dynamically
        create new attributes"""

    __slots__ = ["first_name"]

    pass
