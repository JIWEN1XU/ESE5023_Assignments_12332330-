#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:55:27 2023

@author: xujiwen
"""

def Find_expression(n) :
    str = ["1","2","3","4","5","6","7","8","9"]
    sym = ["+" , "-" , ""]
    sum_n = []
    for a in sym:
        for b in sym:
            for c in sym:
                for d in sym:
                    for e in sym:
                        for f in sym:
                            for g in sym:
                                for h in sym:
                                    sum = str[0] + a + str[1] + b + str[2] + c + str[3] + d + str[4] + e + str[5] + f + str[6] + g + str[7] + h + str[8]
                                    if eval(sum) == n:   # i found this function on the internet
                                        sum_new = sum + "=" + '{}'.format(n)  # my friend told me this function
                                        print(sum_new)
                                        sum_n.append(sum_new)                                       
    return sum_n


   
n = int(input("Please input an integer between 1 and 100:"))

y = Find_expression(n)
print(y)

Total_solutions = [0]*100
for i in range(100):
    #print(i)
    y = Find_expression(i+1)
    Total_solutions[i]=len(y)
    
print(Total_solutions)

# i found this function on the internet
import matplotlib.pyplot as plt
x=range(1,101)
print(x)
plt.plot(x,Total_solutions,"r+-")

import numpy as np
max1=np.max(Total_solutions)
idx= np.where(Total_solutions==max1)

x_new=np.array(x)
x_new[idx]
print("max =",max1 ,", appear at",x_new[idx])


min1=np.min(Total_solutions)
idx= np.where(Total_solutions==min1)

x_new1=np.array(x)
x_new1[idx]
print("min =",min1 ,", appear at",x_new1[idx])

