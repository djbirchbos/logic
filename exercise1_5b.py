# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:35:47 2018

@author: birchd
"""


for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

