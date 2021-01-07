#!/bin/usr/python3
'''
    A function that divide a matrix
    Functions:
        matrix_divided()
'''


def matrix_divided(matrix, div):
    '''
    Args:
        matrix: the symmetric matrix of integers/floats
        div: the integer/float divisor
    Returns:
        The divided matrix
    Raises:
        TypeError:
        If the matrix's rows aren't equal,
        the matrix's items aren't int or float,
        or div's different to int or float
        ZeroDivisionError:
        If div is equal to zero
    '''

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        columns_len = 0
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix.append(round(item / div, 2))
            columns_len += 1
        if len(matrix[0]) != columns_len:
            raise TypeError("Each row of the matrix must have the same size")
    return new_matrix
