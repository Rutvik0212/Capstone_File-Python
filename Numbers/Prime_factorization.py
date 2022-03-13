# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 13:07:15 2022

@author: Rutvik
"""

def prime_fact(num):
    
    # creating list of prime numbers 
    list_prime = []
    
    for i in range(2,num):
        for j in range(2,i):
            if i % j == 0 :
                break 
        else:
            list_prime.append(i)
            
     # find the prime factors of given numbers 
       
    ans_list = []                 # assigning empty list 
    for i in list_prime:
        while num % i == 0:
            num = num / i
            ans_list.append(i)
        if num in list_prime:
            ans_list.append(int(num))
            break
    print(*ans_list, sep = '\n') 
    
    print()
    
    for i in set(ans_list):
        count =  ans_list.count(i)
        if count ==1 :
            print(f'{i}*',end = '') 
        else:
            print(f'{i}^{count}')

        
        