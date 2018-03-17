#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 12:44:39 2018

@author: Bill Armstrong
         GitHub:  Libbyddap
"""

def myfunc(*args):
    print(args)
    return sum(args)*.05

def myfunc2(*args, **kwargs):
    print(args, kwargs)
    print("I would like {} {}".format(args[0], kwargs['food']))

print(myfunc(40, 60, 100, 43, 543, 23, 42))
print(myfunc2(10, 20, 30, fruit='oragne', food="eggs", animal="dog"))
