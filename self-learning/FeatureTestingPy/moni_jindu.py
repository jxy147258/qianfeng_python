# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 14:46:14 2018

@author: jixiaoyun
"""

for i in range(101):
    if i%10 == 0 and i != 100:
        print(i,end='')
    elif i ==100:
            print('Done')
    else:
        print('=',end='')