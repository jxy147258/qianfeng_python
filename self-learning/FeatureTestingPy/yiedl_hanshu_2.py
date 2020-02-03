# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 16:12:11 2018

@author: jixiaoyun
"""

def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 
for n in fab(5):
    print(n)