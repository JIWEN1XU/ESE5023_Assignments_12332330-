#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 00:09:33 2023

@author: xujiwen
"""

# 2.1

import numpy as np
m1 = np.random.randint(low = 51, size = (5,10))
print(m1)
m2 = np.random.randint(low = 51, size = (10,5))
print(m2)

# 2.2

def Matrix_multip(a1, a2):
    arr = np.zeros((5,5))
    for i in range(5):
        for j in range(10):
            for k in range(5):
                arr[i,k] = a1[i,j] * a2[j,k]
    print (arr)

Matrix_multip(m1, m2)