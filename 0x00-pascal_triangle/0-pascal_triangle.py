#!/usr/bin/python3
"""Contains a function that generates
the coefficients of an nth Pascal's Triangle"""


def factorial(n):
    """Calculates the factorial of a given number"""
    if n < 0:
        return None

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def pascal_triangle(n):
    """ generates the coefficients of an nth Pascal's Triangle"""
    triangle = []

    if n <= 0:
        return triangle

    for x in range(n):
        row = []
        for y in range(x + 1):
            row.append(int(factorial(x) / (factorial(y) * factorial(x - y))))
        triangle.append(row)

    return triangle
