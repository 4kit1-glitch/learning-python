#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:29:20 2026

@author: kit
"""


link1 = "www.startimes.com"
link2 = "https://www.manyco.ltd"

# getting website name annd domain

def get_subsrings(text: str) -> tuple[list, int]:
    return [text[: i] for i in range(len(text))]
    pass
def is_substring(string: str, text) -> bool:
    substrings = get_subsrings(text)
    return string in substrings

def clean_link(link: str) -> str:
   PREFIX = ["www.", "https://www."]   
   for string in PREFIX:
       if is_substring(string, link):
           return link.removeprefix(string)

print(clean_link(link1))
print(clean_link(link2))
       
    
        