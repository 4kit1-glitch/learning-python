#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:49:28 2026

@author: kit
"""

def dot(l1, l2):
    return sum(num1 * num2 for num1, num2 in zip(l1, l2))

def dot2(l1, l2):
    sum = lambda x, y: x + y
    return list((sum, zip(l1, l2)))


l1 = [1, 2, 3]
l2 = [2, 4, 1]
print(dot(l1, l2), dot2(l1, l2))
