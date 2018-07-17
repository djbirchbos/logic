# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:35:47 2018

@author: birchd
"""

x = int(input('Enter a number: '))

if x % 2 != 0 and x % 3 == 0:
    print('Odd and divisible by 3')
elif x % 2 == 0 and x % 3 == 0:
    print('Even and divisible by 3')
elif x % 2 != 0:
    print('Odd')
elif x % 2 == 0:
    print('Even')