# !/usr/bin/env python3

'''
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def palindromic(v):

    if str(v) == str(v)[::-1]:
        return True
    else:
        return False

nums = ( i * v for i in range(100,1000) for v in range(i,1000))

print("Result",max(filter(palindromic,nums)))