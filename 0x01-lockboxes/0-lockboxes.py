#!/usr/bin/python3
"""This script contain a method that determines,
if all boxes can be opened in an array of boxes"""


def canUnlockAll(boxes):
    """return a boolean depending on the boxes"""
    all_keys = {}
    if len(boxes) > 1:
        for box in boxes:
            for key in box:
                all_keys[key] = key

        list_all_keys = sorted(list(all_keys.keys()))
        if list_all_keys[0] == 0:
            list_all_keys = list_all_keys[1:]
        for i in range(1, len(boxes)):
            if list_all_keys[i - 1] == i and len(boxes[i - 1]) != 0:
                continue
            else:
                return False
    return True
