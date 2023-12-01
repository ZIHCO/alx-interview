#!/usr/bin/python3
"""This module contain a definition, pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the pascal's
    triangle of n"""

    new_list = []
    if n <= 0:
        print("hello")
        return new_list
    m = 1
    if n == 1:
        new_list.append([1])
        return new_list
    if n > 1:
        while m <= n:
            i = 0
            sub_list = []
            while i < m:
                if i == 0:
                    sub_list.append(1)
                elif (i + 1) == m:
                    sub_list.append(1)
                else:
                    sub_list.append((last_list[i - 1]
                                    + last_list[i]))
                i += 1
            last_list = sub_list[:]
            new_list.append(sub_list)
            m += 1
        return new_list
