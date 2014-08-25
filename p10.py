# !/usr/bin/env python3

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''


def gen_primes():
    '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2  # first integer to test for primality
    while True:
        if q not in D:
            yield q  # not marked composite, must be prime
            D[q * q] = [q]  # first multiple of q not already marked
        else:
            for p in D[q]:  # move each witness to its next multiple
                D.setdefault(p + q, []).append(p)
            del D[q]  # no longer need D[q], free memory
        q += 1


from itertools import takewhile

print("Result:",
      sum(takewhile(lambda x: x < 2000000, gen_primes())))