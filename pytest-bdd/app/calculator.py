"""Minimal calculator module used by BDD tests."""

def add(a, b):
    """Return sum of two numbers."""
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
