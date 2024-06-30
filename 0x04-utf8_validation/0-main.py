#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8
to_bin = __import__('0-validate_utf8').to_bin

data = [235, 140]
print(validUTF8(data))

data = [345, 467]
print(validUTF8(data))

data = [250, 145, 145, 145, 145]
print(validUTF8(data))
