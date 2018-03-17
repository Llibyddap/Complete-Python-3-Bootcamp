#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 22:15:19 2018

@author: bill
"""

import unittest
import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
        
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')
        
if __name__=='__main__':
    unittest.main()