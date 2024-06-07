#!/usr/bin/python3
"""contains the canUnlockAll function"""
import sys


sys.setrecursionlimit(1500)


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    if type(boxes) is not list or len(boxes) == 0:
        return False
    return validate_array(check_boxes(boxes, [0 for _ in boxes], 0))


def validate_array(array):
    """checks if all elements in an array are equal to 1"""
    for i in array:
        if i != 1:
            return False
    return True


def check_boxes(boxes, array, index):
    """opens a box and checks if the box contains keys
    if it does, it sets the value of the box to 1"""
    array[index] = 1
    for x in boxes[index]:
        if x >= len(boxes) or array[x] == 1:
            continue
        array = check_boxes(boxes, array, x)
        if validate_array(array):
            return array
    return array
