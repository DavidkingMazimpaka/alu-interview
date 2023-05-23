#!/usr/bin/python3
"""
minimum operations
"""


def minOperations(n):
    """
    func to return the fewest op
    """
    operations = 0
    d = 2

    while n > 1:
        if n % d == 0:
            operations += d
            n /= d
        else:
            d += 1

    return operations
