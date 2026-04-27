#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:17:56 2026

@author: kit
"""

#handles the zerodivision error and valur error and return gracefully

try:
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    result = num1 / num2
    print(result)
except (ValueError, ZeroDivisionError) as e:
    print(f"unexpected error {e}")
    