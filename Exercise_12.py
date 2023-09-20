# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:50:07 2023

@author: salsi
"""

'''Create a function that receives a list of floating numbers as its input and returns
the sum of all its elements. '''

def floatingSum(list):
    tot = 0.0
    for i in list:
        tot = tot + i
    return tot