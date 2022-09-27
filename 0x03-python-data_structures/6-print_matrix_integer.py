#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if col != row[-1]:
                print("{:d}".format(matrix[row][col]), end=" ")
            else:
                print("{:d}".format(matrix[row][col]), end="")
        print()
