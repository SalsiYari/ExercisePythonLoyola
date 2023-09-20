# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 16:47:12 2023

@author: salsi
"""
print()
l=list()

pizza = {'Name': "diavola", 'Ingredients': ["tomato sauce", "mozzarella","salamino spicy"], 'Price': 6}
print("the pizza is:\n",pizza)
#Use a method to create a list including only the values of the keys
for i in pizza.keys():
    l.append(i)
print("the list is:\n",l)



