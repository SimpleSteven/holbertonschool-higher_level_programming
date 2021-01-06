#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    def multiply_by_2(num1):
        return num1 * number
    new_list = list(map(multiply_by_2, my_list))
    return new_list
