#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations
isPrimeNumber = __import__('0-minoperations').isPrimeNumber
lowestCommonMultiples = __import__('0-minoperations').lowestCommonMultiples

# print(isPrimeNumber(11))
# print(isPrimeNumber(15))
# print(isPrimeNumber(17))
# print(isPrimeNumber(23))
# print(isPrimeNumber(35))
# print(isPrimeNumber(71))
# print(isPrimeNumber(97))
# print(isPrimeNumber(196))

# print(lowestCommonMultiples(12))
# print(sum(lowestCommonMultiples(12)))


n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 21
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 7
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 8
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
