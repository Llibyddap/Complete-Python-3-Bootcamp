#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 14:45:04 2018

@author: Bill Armstrong
         GitHub:  Libbyddap
"""

b = [[1,1],[1,0]]
a = [[0]*2]*2
for i in range(2):
    for j in range(2):
        a[i][j] = b[i][j]
        print ("A: ", a, "B:", b)
print(b)
print(a)