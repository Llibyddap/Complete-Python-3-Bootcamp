#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 22:49:57 2018

@author: Bill Armstrong
         GitHub:  Libbyddap
"""

import one

print("TOP LEVEL IN TWO.PY")

one.func()

if __name__=='__main__':
    print("TWO.PY is being run directly")
else:
    print("ONE.PY has been imported")