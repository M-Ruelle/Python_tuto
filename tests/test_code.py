# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:25:37 2024

@author: Lenovo
"""
from chekio.mult_two import mult_two

def test_multiply():
    
    a = 12
    b = 6
    
    assert mult_two(a, b) == a*b
    
    
