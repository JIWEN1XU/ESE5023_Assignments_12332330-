#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:46:23 2023

@author: xujiwen
"""

# 3
def Pascal_triangle(k):
    triangle = []
    for i in range(k):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    print_pascals_triangle(triangle, k)

def print_pascals_triangle(triangle, k):
    index = 0
    for row in triangle:
        index += 1
        if index == k:
            print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))
            


Pascal_triangle(100)
Pascal_triangle(200)
