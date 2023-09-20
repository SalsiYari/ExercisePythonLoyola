# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:43:07 2023

@author: salsi
"""

def isPalindrome(s):
    lng = len(s)
    i = 0
    statement=False
    
    if(lng % 2 == 1):
        #odd
        for i in range(0, int(lng/2)):
            if(s[0+i] != s[-1-i]):      #stop condition
                break
            if((2+i) == (int(lng/2) + 1)):  # every char
                statement = True
            else:                           #break before the finish

                statement = False
    if(lng % 2 == 0):
        #even
        for i in range(0, int( lng / 2 )):
            if(s[0+i] != s[ - 1 - i ]):
                break
            if(( 0 + i ) == ((lng / 2 ) - 1 )):    #for every char
                statement = True
            else:
                statement = False
    return statement



'''
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:44:13 2023

@author: salsi
"""
import Exercise8 as pippo
#main
w = input("Insert the word\n >")
print("the result of isPalindrome() -> " + str(pippo.isPalindrome((w))))

'''


         
     
           
    