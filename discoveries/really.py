#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 23:13:06 2026

@author: kit
"""
#printing elements in a list

nums = [1, 3, 4, 5, 0, 8, 76, 45]

# really short way to print items in a collection
# it is very short but expensive
# it uses a list and a tuple of each element in the collection
# *nums can be separated with any iterable
print(*"hello", sep=",")

def select_even(num):
    """
    Parameters
    ----------
    num : TYPE
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    return num % 2 == 0

evens = list(filter(select_even, nums))
print(evens)

odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)
