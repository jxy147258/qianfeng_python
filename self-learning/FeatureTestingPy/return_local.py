# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 14:54:00 2018

@author: jixiaoyun
"""

m,n = 3,5
print(id(m),id(n))
m,n = n,m
print(id(m),id(n))