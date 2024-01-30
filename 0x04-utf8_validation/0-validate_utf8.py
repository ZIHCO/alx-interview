#!/usr/bin/python3
"""contains the definitions validUTF8"""


def validUTF8(data):
    """return a boolean to validate data utf8"""
    if type(data) is list:
        for element in data:
            if type(element) is int and (element < 255):
                continue
            else:
                return False
        return True
    return False
