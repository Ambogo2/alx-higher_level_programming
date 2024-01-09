#!/usr/bin/python3
"""A module containing save_to_json_file function."""


def pascal_triangle(n):
    """
    pascal_triangle - generates Pascal's triangle of n rows
    args:
        n: number of rows in the Pascal's triangle
    returns:
        list of lists of integers representing the  Pascal's triangle
    """
    if n <= 0:
        return []

    result = [[1]]
    for i in range(n - 1):
        temp = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[- 1]) + 1):
            row.append(temp[j] + temp[j + 1])
        result.append(row)
    return result
