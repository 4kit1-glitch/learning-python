#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 05:50:32 2026

@author: kit
"""

"""
arbituary arguments : *args
passes a tuple of arguements

arbituary keyword arguments passes a dictionary of arguments
: **kargs
passes a dict of keyword args
use when the number of key word arsg is unknown
"""

def set_default_setting(**settings):
    print(settings)
    settings["level"] = 1
    settings["play"] = False
    settings["speed"] = "slow"
    print(settings)

set_default_setting(level = 18, play = True, speed = "fast")