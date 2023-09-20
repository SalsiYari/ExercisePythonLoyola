# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:34:55 2023

@author: salsi
"""

print()

#class studente
class Student(object):
    rep= False
    def __init__(self,age,email,marks,absences):
        self.age=age
        self.email=email
        self.marks=marks
        self.absences=absences
    
    def sMark(self):
        sum=0
        for i in self.marks:
            sum=sum+i
        return (sum/(len(self.marks)))
    
    def absent(self):
        if(self.absences > 5):
            return True
        else:
            return False
#---------main--------
s1 = Student(20, "s1.com", [2,3,2], 10)
s2 = Student(21, "s2.com", [7,8,5], 2)
s3 = Student(20, "s3.com", [5,4,9], 6)
s4 = Student(22, "s3.com", [3,2,1], 1)

s2.rep = True
s4.rep = True


students = [s1, s3, s4]
print("fatto")


f=open("file_ex_18.txt","w")
for i in students:
    if(i.sMark() < 5):
        f.write(str(i.age)+" ")
        f.write(str(i.email) + " ")
        f.write(str(i.marks) + " ")
        f.write(str(i.absences) + " ")
        f.write(str(i.rep) + " ")
    f.write("\n")
f.close()




            
