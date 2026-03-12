#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function: Recursively computes the factorial of a given number.

    Parameters:
    n (int): The non-negative integer to compute the factorial of.

    Returns:
    int: The factorial of n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
