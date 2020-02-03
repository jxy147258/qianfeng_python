# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:15:44 2018

@author: jixiaoyun
"""

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = print("please input your number: ",input())
print(n)