# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 17:51:35 2022

@author: Rutvik
"""

def binary_to_decimal(num):
    num = str(num)
    print (int(num , 2))
    

def decimal_to_binary(num):
    
    binary_list = []
    while num != 0:
        ans = num % 2
        num = num //2
        binary_list.append(ans)
    binary_list.reverse()
    for i in binary_list:
        print(i , end = ' ')