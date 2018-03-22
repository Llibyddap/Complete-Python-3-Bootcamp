#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 12:47:14 2018

@author: Bill Armstrong
         GitHub:  Libbyddap
"""

from traits.api import HasTraits, Str, Int
import traitsui

class SimpleEmployee(HasTraits):
    frist_name = Str
    last_name = Str
    department = Str
    
    employee_numer = Str
    salary = Int
    

sam = SimpleEmployee()
sam.configure_traits()
