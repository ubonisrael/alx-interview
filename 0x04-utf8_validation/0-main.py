#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8
to_bin = __import__('0-validate_utf8').to_bin

data =  [467, 133, 108]
print(validUTF8(data))
