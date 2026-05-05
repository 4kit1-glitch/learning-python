#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 23:09:51 2026

@author: kit
"""

current_settings = {
    "theme": "light",
    "font": "nano",
    "style": 9
}

user_config = {
    "theme": "dark",
    "font": "nano",
    "style": 12
}

print(current_settings)
# this updates all the values in current settings where the keys match
current_settings |= user_config
print(current_settings)