# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 12:25:02 2022

@author: Rutvik
"""

def fab_series(num):
    
    series_list = []
    a = 0
    b = 1
    c = 0 
    
    for i in range(num):
        c = a + b
        a = b
        b = c
        series_list.append(c)
    
    return (series_list)

    