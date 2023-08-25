# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:19:42 2023

@author: LAB
"""

a = float(input('1st number:'))
b = float(input('2nd number:'))
c = float(input('3rd number:'))
if a+b<=c or a+c<=b or b+c<=a or a==0 or b==0 or c==0:
    
    print('they dont form a triangle')
else:
    print('they form a triangle')
    