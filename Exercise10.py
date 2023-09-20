# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:46:09 2023

@author: salsi
"""
print()
l1 = [3 , 4 , 2 , 3 , 5]
l2 = [ 3 , 4 , 2 , 3 , 5]

def comparaList(la, lb):
    out = False
    if(len(la) == len(lb)):
        out = True
        i = 0
        
        while(i < len(la)):
            
            if(la[i] != lb[i]):
                out = False
                break
            else:
                i = i +1
    return out

print("Result of comparaList function is :\n " + str(comparaList(l1, l2)))