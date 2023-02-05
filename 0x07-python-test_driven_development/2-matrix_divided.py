#!/usr/bin/python3
"""definition for matrix_divided function"""


def matrix_divided(matrix, div):
    """
     function that divides all elements of a matrix.

     Parameters:
        matrix:  list of lists of integers or floats
        div: the divisor that must be an int or float.
    """
    if isinstance(matrix, list):
        pass
    else:
        raise TypeError("matrix must be a matrix (list of lists) of " +
                        "integers/floats")
    for index in range(len(matrix)):
        if isinstance(matrix[index], list) or len(matrix[index]) == 0:
            row_size = len(matrix[0])
        else:
            raise TypeError("matrix must be a matrix (list of lists) of " +
                            "integers/floats")
        if not len(matrix[index]) == row_size:
            raise TypeError('Each row of the matrix must have the same size')
        for item in range(row_size):
            if type(matrix[index][item]) not in [float, int]:
                raise TypeError("matrix must be a matrix (list of lists) of " +
                                "integers/floats")
