#!/usr/bin/python3
"""
Main file for testing
"""
import time

makeChange = __import__('0-making_change_1').makeChange


print(makeChange([10, 15, 2, 1], 50))
print(makeChange([10, 3], 24))

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

