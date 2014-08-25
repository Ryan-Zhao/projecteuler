# !/usr/bin/env python3

'''
Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
'''

sum_of_square = sum(map(lambda x: x ** 2, range(1, 101)))
square_of_sum = sum(range(1, 101)) ** 2
print("Result:", sum_of_square - square_of_sum)

