#!/usr/bin/python3
"""Contains the to_bin and validUTF8 functions"""


def to_bin(n):
    """Converts a number to binary"""
    arr = []
    while n > 0:
        arr.append(n % 2)
        n = n // 2
    while len(arr) < 8:
        arr.append(0)
    arr = list(reversed(arr))
    return arr


def validUTF8(data):
    """Checks if the given data set is a valid UTF-8 encoding"""
    # set a variable that holds the number of continued bytes
    continued_bytes = 0
    for dat in data:
        if type(dat) is not int:
            return False
        bin = to_bin(dat)  # convert number to binary
        if continued_bytes > 0:  # check if byte is a continued byte
            if bin[0] == 1 and bin[1] == 0:
                continued_bytes -= 1
                continue
            return False
        if bin[0] == 0:
            continued_bytes = 0
            continue
        if bin[1] == 1:
            if bin[2] == 1 and bin[3] == 0:
                continued_bytes = 1
                continue
            if bin[2] == 1 and bin[3] == 1 and bin[4] == 0:
                continued_bytes = 2
                continue
            if bin[2] == 1 and bin[3] == 1 and bin[4] == 1 and bin[5] == 0:
                continued_bytes = 3
                continue
            return False
    return True
