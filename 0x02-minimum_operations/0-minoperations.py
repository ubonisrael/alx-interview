#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can
execute only two operations in this file: Copy All and Paste. Given
a number n, write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""
from typing import List


def isPrimeNumber(n: int) -> bool:
    """
    checks if a number is a prime number
    """
    x = 2

    while x <= (n / x):
        if n % x == 0:
            return False
        x += 1
    return True


def LCM(n: int, x: int = 2, array: List[int] = []) -> List[int]:
    """
    returns an array of the lowest common multiples of a number
    """
    if n == 1:
        return array

    while x <= n:
        if n % x == 0:
            array.append(x)
            return LCM(n / x, x, array)
        x += 1
    return array


def minOperations(n: int) -> int:
    """
     a function that calculates the fewest number of operations
     needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    # check if n is a prime number
    if isPrimeNumber(n):
        return n

    # get the lowest common multiples of the number
    # sum them up and return
    # Note, all LCMs will be prime numbers
    return sum(LCM(n, 2, []))
