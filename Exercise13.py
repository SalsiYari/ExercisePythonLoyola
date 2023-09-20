# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:42:14 2023

@author: salsi
"""
print()
'''
Based on the function created in Exercise (12), create a function that multiplies
all the elements located at odd positions of the list. The function should work for
any list length. The first position of the list (0 position) will be considered as odd.'''

def OfAllElements(lista):
    sm = 1
    for i in range(0, len(lista)):
        if(((i % 2) != 0) or (i == 0)):
            sm = lista[i] * sm
        
    return sm

'''

list = [3.2, 3.0, 1.250]
print("Result of list -> " + str(OfAllElements(list)))'''