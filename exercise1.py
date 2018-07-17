# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:35:47 2018

@author: birchd
"""

x = int(input('Enter a number: '))

if x < 10:
    print('This is a good number')
elif x > 9 and x < 100:
    print('This is a better number')
elif x > 9 and x < 100 and x / 2 == 0:
    print('This is the best number')
else:
    print('Horrible')