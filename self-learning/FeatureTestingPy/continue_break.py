# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 17:27:32 2018

@author: jixiaoyun
"""

for i in range(10):
    if i%2 != 0:
        print('nei')
        continue #结束本次循环
        #break #结束整个循环
    i += 2
    print(i,'wai')