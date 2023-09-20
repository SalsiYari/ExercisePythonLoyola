# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:05:08 2023

@author: salsi
"""

print()
'''
Create a function that receives an integer number as its input and returns True
if the number is prime and False if it is not. '''

from math import sqrt 

def prime():
    
    n=int(input("inserisci un numero>"))
    
    if(n <= 1):
        out = False
        
    else:
        for i in range(2, int(sqrt(n))+1):
            if(n % i == 0):
                out = False
            else:
                out = True
    return out

#main
print("Result of isPrime() ->\n " + str(prime()) )
                    
            