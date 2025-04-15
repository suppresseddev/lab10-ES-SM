# https://github.com/suppresseddev/lab10-ES-SM
# Partner 1: Eli Simon
#Partner 2: Santiago Mena
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
def mul(a, b): return a * b
def div(a, b):
    if b == 0: raise ValueError
    return a / b
def logarithm(a,b):
    if a == 0 or b == 0:
        raise ValueError
    return log(b, a)
def exp(a,b):
    return a**b