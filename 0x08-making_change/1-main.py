#!/usr/bin/python3
"""
Main file for testing
"""
import time

makeChange = __import__('0-making_change_1').makeChange

st = time.time()
print(makeChange([10, 15, 2, 1], 50))
end1 = time.time()
print(makeChange([1, 2, 25], 37))
end2 = time.time()
print(makeChange([1256, 54, 48, 16, 102], 1453))
end3 = time.time()
print(end1 - st)
print(end2 - end1)
print(end3 - end2)
