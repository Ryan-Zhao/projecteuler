# !/usr/bin/env python3

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
 remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from functools import reduce


def factors(v):
    i = 2
    while i < v:
        if v % i:
            i += 1
        else:
            yield i
            v //= i
    yield v


def product(x, y):
    for i in factors(y):
        if x % i:
            x *= i
    return x


print("Result:", reduce(product, range(2, 11),1))
