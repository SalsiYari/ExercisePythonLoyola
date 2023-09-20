# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:06:34 2023

@author: salsi
"""
print()

#Using the input() command and the if-else sentences, determine if the first
#number of your DNI is greater or smaller than the last one.


dni = input("Insert your dni:\n")
if(dni[0] > dni[-1]):
    print("the first number of DNI is greater  then the last one\n ")
else:
    print("The first number of DNI is smaller than the last one\n")
        
