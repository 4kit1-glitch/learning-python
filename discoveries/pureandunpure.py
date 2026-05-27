#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:23:34 2026

@author: kit
"""

"""
    a pure function is a function that
    1. always returns the same output for any input class
    2. has no side effects that is it doesnt modify anything outside the                                    function

"""

# pure function
def add(a, b):
    return a + b


total = 0

def add_to_total(x):
    global total # take note of this program wont run without it
    total += x

add_to_total(5)
print(total)
add_to_total(3)
print(total)