#!/usr/bin/python3
import sys

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = []
limit = 1000

for i in range(1, limit):
    keys = []
    for i in range(1, limit):
        keys.append(i)
    boxes.append(keys)
print(sys.getrecursionlimit())
print(canUnlockAll(boxes))

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes))

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6], [7]]
# print(canUnlockAll(boxes))

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes))
