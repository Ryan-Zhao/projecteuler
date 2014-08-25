# !/usr/bin/env python3

'''
What is the 10 001st prime number?
'''

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

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


from itertools import islice

print("Result:", next(islice(gen_primes(), 10000, 10001)))
