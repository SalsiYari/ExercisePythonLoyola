# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:12:45 2023

@author: salsi
"""
print()
dni = [5,9,6,9,4]
max = dni[0]
min = dni[0]
i = 0
position=0;
position2=0;
'''Create a list with the numbers of your DNI. Using a for loop and the if
sentence, determine the highest number and its position within the DNI. If there
are two or more positions featuring the highest number, indicate all of them. '''
lng=len(dni)

print(len(dni))
for i in range(lng):
    if(dni[i] > max):
        max = dni[i]
        
print()
print(">the maximum number of the list is ", max)
for i in range(lng):
    if(dni[i] == max):
        print(">Position of the number ",i)


                        