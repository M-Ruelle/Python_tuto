# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:25:37 2024

@author: Lenovo
"""
#import sys

#sys.path.append(r"C:\Users\Lenovo\Desktop\py_files\chekio")

from chekio.Multiply import mult_two

def test_multiply():
    
    a = 12
    b = 6
    
    assert mult_two(a, b) == a*b
    
    
