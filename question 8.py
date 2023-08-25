# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:12:04 2023

@author: LAB
"""

basic = float(input('type the basic salary:'))
hra = basic/5
ta = basic/20
da = basic/10
gross = basic+hra+ta+da
print('gross salary is :',gross)