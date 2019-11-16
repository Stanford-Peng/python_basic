#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:26:34 2019

@author: stanford
"""

amount = input("How many numbers do you want to input: ")
numbers = []

for i in range(0, int(amount)):
    number = input("Please enter an integer: ")
    numbers.append(int(number))    

#with order of pair and dupicate pair
for number1 in numbers :
    for number2 in numbers:
        if (number1 * number2) % 2 == 0 and (number1 + number2) % 2 != 0 :
            print(number1,"--", number2)

#without duplicates and order
output = []            
for number1 in numbers :
    for number2 in numbers:
        if (number1 * number2) % 2 == 0 and (number1 + number2) % 2 != 0 and (number1,number2) not in output:
            output.append((number1, number2))

for pair1 in output:
    for pair2 in output:
        if pair1[0] == pair2[1] and pair1[1] == pair2[0]:
            output.remove(pair2)

for pair in output:
    print(pair)