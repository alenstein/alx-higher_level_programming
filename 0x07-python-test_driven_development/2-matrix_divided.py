#!/usr/bin/python3
"""
    Module for function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
        definition for function that returns a new matrix,
        All elements of the matrix should be divided by div,
        rounded to 2 decimal places.
        Args:
        matrix: must be a list of lists of integers or floats.
        div: must be a number (integer or float).
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
                
