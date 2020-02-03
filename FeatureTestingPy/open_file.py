# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 17:57:11 2018

@author: jixiaoyun
"""

f = open("result.txt","r")
for i in range(10):
    print(str(i)+"行"+f.read()) #读出来的内容是一行一行的
f.close()