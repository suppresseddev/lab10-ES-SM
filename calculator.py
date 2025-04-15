"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
from math import *
# First example
def square_root(a):
    if a < 0:
        raise ValueError
    return sqrt(a)
def hypotenuse(a, b):
    return hypot(a, b)
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def logarithm(a,b):
    if a == 0 or b == 0:
        raise ValueError
    return log(b, a)
def exponent(a,b):
    return a**b

