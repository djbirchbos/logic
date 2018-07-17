# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:35:47 2018

@author: birchd
"""

numbers = list(range(1,100))
numbers2 = []

for i in numbers: 
    if int(i) % 3 == 0 and int(i) % 5 == 0:
        numbers2.append('FizzBuzz')
    elif int(i) % 3 == 0:
        numbers2.append(str('Fizz'))
    elif int(i) % 5 == 0:
        numbers2.append(str('Buzz'))
    else:
        numbers2.append(i)
   
print(numbers2)

