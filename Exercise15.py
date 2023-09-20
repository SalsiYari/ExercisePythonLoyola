# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:19:20 2023

@author: salsi
"""

print()
''') Given the following list: ["a", 1, [1,2], 2, (1,2), 3], create a function that returns a
list including only the integer elements from the original list. 
 '''
 
def newList(lista):
    ret = list()
    for i in lista:
        i=str(i)
        if(i.isnumeric()  ):
            ret.append(i)
    return ret
'''
l = ["a",1,[1,2],2,(1,2),3]
lista=newList(l)
print(lista)'''