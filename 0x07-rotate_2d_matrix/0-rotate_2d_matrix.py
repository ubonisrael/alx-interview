#!/usr/bin/python3
"""rotate_2d_matrix module"""


def rotate_2d_matrix(matrix):
    """rotates a 2d matrix by 90deg"""
    n = len(matrix)
    mat_copy = [row[:] for row in matrix]
    for i in range(n):
        for j in range(n):
            matrix[j][n-i-1] = mat_copy[i][j]