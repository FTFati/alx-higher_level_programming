#!/usr/bin/python3
'''
function that divides all elements of a matrix
'''


def matrix_divided(matrix, div):
    '''divides all elements of a matrix'''
    mat = []

    if div is None or type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        inside = []
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int\
               and type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            if len(matrix[0]) != len(matrix[i]):
                raise TypeError("Each row of the matrix"
                                " must have the same size")
            inside.append(round((matrix[i][j]) / div, 2))
        mat.append(inside)
    return mat
