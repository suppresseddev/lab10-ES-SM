"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return ZeroDivisionError

def log(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        return ValueError

def exp(a, b):
    return a**b


