# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:26:42 2023

@author: salsi
"""
print()
''' Create a function that receives a list and a tuple as its inputs and
returns True if the tuple is greater than the list and False otherwise. The list and'''

def comparization(lista, tupla):
    if(len(tupla)>len(lista)):
        dim= len(tupla)
    else:
        dim=len(lista)
    for i in range(0, dim):
        if(tupla[i] > lista[i]):
            return True
        elif(lista[i] < tupla[i]):
            return False
        
lista=[3,4,5,6]
tupla=(3,4,5,6)
tupla1=(4,5,6,7)
print(comparization(lista, tupla)   )
