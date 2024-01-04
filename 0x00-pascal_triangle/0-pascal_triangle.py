#!/usr/bin/python3
"""script contains a the pascal triangle function"""


def pascal_triangle(n: int):
    """the pascal triangle function returns
    a list."""
    if n <= 0:
        return []
    list_rows = []
    previous_row = []
    for i in range(1, n + 1):
        if len(list_rows) > 0:
            previous_row = row
        row = []
        j = 0
        while j <= i:
            if j == 0:
                row.append(1)
            elif len(row) == i - 1:
                row.append(1)
            elif previous_row:
                k = 1
                while k < len(previous_row):
                    k_entry = previous_row[k] + previous_row[k - 1]
                    row.append(k_entry)
                    k += 1
                    j += 1
            j += 1

        list_rows.append(row)
    return list_rows
