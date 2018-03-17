#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 22:49:45 2018

@author: Bill Armstrong
         GitHub:  Libbyddap
"""

def func():
    print("FUNC() IN ONE.PY")
    
print("TOP LEVEL IN ONE.PY")

if __name__=='__main__':
    print("ONE.PY is being run directly")
else:
    print("ONE.PY has been imported")