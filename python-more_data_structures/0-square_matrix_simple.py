#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []

    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num ** 2)
        square_matrix.append(new_row)

    return square_matrix

# return [[num ** 2 for num in row] for row in matrix]
