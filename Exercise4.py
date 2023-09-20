# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 16:40:34 2023

@author: salsi
"""
print("\n")
s="www.marca.com"
print(">the given string is:")
print("www.marca.com")
'''
Use the strip method to convert a string expressed as an URL (for instance,
“www.marca.com”) into the equivalent string without “www.” and “.com”. Note:
use more than one line of code if necessary. 
'''
s1 = s.strip('.com')
s1 = s1.strip("w.")
print(">the result is:")
print(s1)
