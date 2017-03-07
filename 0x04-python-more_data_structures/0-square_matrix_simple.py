'''
The function in this file computes the square value of all integers of a matrix.
'''

def square_matrix_simple(matrix=[]):
    return [[num**2 for num in elem] for elem in matrix]
