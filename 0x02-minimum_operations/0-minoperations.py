#!/usr/bin/python3
"""In a text file, there is a single character H.

Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method
that calculates the fewest number of operations needed to
result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH =>
    Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n: int):
    """Minimum Operations."""
    _primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                  59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
                  127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                  191, 193, 197, 199, 211, 223, 227, 229])
    max_prime = 229
    if n < 4:
        return n

    def prime_factor(num):
        """Find least prime factor of num."""
        if num in _primes:
            return num
        for prime in _primes:
            if num % prime == 0:
                return prime
        nonlocal max_prime
        if num < (max_prime * 3):
            return num
        tmp = max_prime + 1
        while num > (2 * tmp):
            is_prime = True
            for prime in _primes:
                if tmp % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                _primes.add(tmp)
                max_prime = tmp
                if num % tmp == 0:
                    return tmp
            tmp += 1

    factors = []
    tmp = n
    while True:
        factor = prime_factor(tmp)
        factors.append(factor)
        if factor == tmp:
            break
        tmp /= factor
    return int(sum(factors)
