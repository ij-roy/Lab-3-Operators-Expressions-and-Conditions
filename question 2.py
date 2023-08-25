# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:10:35 2023

@author: LAB
"""
print('units is in kilogram and metres')
w = float(input('write the weight:'))
h = float(input('write the height'))
bmi = w/h/h
print('the bmi is ',bmi) 



print('units is in pounds and inches')
w = float(input('write the weight:'))
h = float(input('write the height'))
e = w*0.453592
j = h*0.0254
bmi = e/j/j
print('the bmi is ',bmi) 