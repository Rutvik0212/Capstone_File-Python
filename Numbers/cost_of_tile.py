# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 17:33:43 2022

@author: Rutvik
"""

def cost_tile():
    
    width = float(input("Enter the Floor Width: "))
    height = float(input("Enter the Floor Height: "))
    cost = float(input("Enter the cost for one tile Rs. "))
    
    return (f'Total cost required for tile to cover the floor is {width * height * cost} rs.')

    