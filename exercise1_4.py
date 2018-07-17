# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:35:47 2018

@author: birchd
"""

x = 0

for i in range(1,50):
    x += i
    print('Total: ', x)
    print('Number: ', i)
    
    if x > 100:
        print('The sum exeeded the max value of 100.  The number that makes the total > 100 is: ', i)
        break