#!/usr/bin/python3
""" This script contains the definition, makeChange"""


def makeChange(coins, total):
    """solves the problem of minimal notes to make a change
    given a set of denominations"""

    sortedCoinsList = sorted(coins, reverse=True)
    count = 0
    for coin in sortedCoinsList:
        if coin < total:
            while coin <= total:
                total -= coin
                count += 1
    if total == 0:
        return count
    return (-1)
