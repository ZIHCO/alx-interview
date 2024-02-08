#!/usr/bin/python3
"""
   This solves the NQueens puzzle challenge
   Usage: nqueens N
"""

import sys


def check_box(i, j, lst):
    if i > 0:
        if j > 0 and j < N - 1:
            if lst[i - 1][j - 1][str([i - 1, j - 1])]:
                return False
            if lst[i - 1][j][str([i - 1, j])]:
                return False
            if lst[i - 1][j + 1][str([i - 1, j + 1])]:
                return False
        if j == 0:
            if lst[i - 1][j][str([i - 1, j])]:
                return False
            if lst[i - 1][j + 1][str([i - 1, j + 1])]:
                return False
        if j == N - 1:
            if lst[i - 1][j - 1][str([i - 1, j - 1])]:
                return False
            if lst[i - 1][j][str([i - 1, j])]:
                return False
    return True


def horizontal(i, j, lst):
    new_lst = lst.copy()
    k = 0
    while k < N:
        if k != j:
            new_lst[i][k][str([i, k])] = False
        k += 1
    return new_lst


def vertical(i, j, lst):
    new_lst = lst.copy()
    k = 0
    while k < N:
        if k != i:
            new_lst[k][j][str([k, j])] = False
        k += 1
    return new_lst


def left_diagonal(i, j, lst):
    new_lst = lst.copy()
    k = i
    m = j
    while m >= 0 and k < N:
        if k != i:
            new_lst[k][m][str([k, m])] = False
        k += 1
        m -= 1
    return new_lst


def right_diagonal(i, j, lst):
    new_lst = lst.copy()
    k = i
    m = j
    while m < N and k < N:
        if k != i:
            new_lst[k][m][str([k, m])] = False
        k += 1
        m += 1
    return new_lst


def recursion(k):
    if k == 2:
        return
    recursion(k - 1)
    c_list = []
    for i in range(N):
        b_list = []
        for j in range(N):
            a_list = []
            dct = {}
            a_list.append(i)
            a_list.append(j)
            dct[str(a_list)] = True
            b_list.append(dct)
        c_list.append(b_list)

    i = 0

    while i < N:
        if i == 0:
            j = k - 2
        else:
            j = 0
        while j < N:
            if i == 0:
                c_list = horizontal(i, j, c_list)
                c_list = vertical(i, j, c_list)
                c_list = left_diagonal(i, j, c_list)
                c_list = right_diagonal(i, j, c_list)
                i += 1
                j = 0
                continue
            elif c_list[i][j][str([i, j])] and check_box(i, j, c_list):
                c_list = horizontal(i, j, c_list)
                c_list = vertical(i, j, c_list)
                c_list = left_diagonal(i, j, c_list)
                c_list = right_diagonal(i, j, c_list)
            j += 1
        i += 1

    result = []
    i = 0
    while i < N:
        j = 0
        while j < N:
            if c_list[i][j][str([i, j])]:
                result.append([i, j])
            j += 1
        i += 1

    print(str(result))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            N = int(sys.argv[1])
        except Exception:
            print("N must be a number")
            exit(1)
        if N < 4:
            print("N must be at least 4")
            exit(1)
        recursion(N)
    else:
        print("Usage: nqueens N")
        exit(1)
