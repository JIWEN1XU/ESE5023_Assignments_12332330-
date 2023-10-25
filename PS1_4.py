#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:09:37 2023

@author: xujiwen
"""


# 4
import random

# I found this function on the internet.
x = random.randint(1,100)

print("x:{}".format(x))

def Least_moves(x):
    
    if (x % 2)==0:
        n = x / 2
    else:
        n = (x-1) / 2 + 1
# My roommate taught me this function to link strings.       
    print("n:{}".format(n))

Least_moves(x)

