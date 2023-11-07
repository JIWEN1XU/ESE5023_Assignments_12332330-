#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:58:20 2023

@author: xujiwen
"""

# 1
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

if a > b :
    if b > c :
        print("a, b, c")
    else:
        if a > c:
            print("a, c, b")
        else:
            print("c, a, b")
else:
    if b > c:
        if a > c :
            print("b, a, c")
        else:
            print("b, c, a")
    else:
        print("c, b, a")
        






