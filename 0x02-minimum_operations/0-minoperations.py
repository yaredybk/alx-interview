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
from typing import Set, List


def minOperations(n: int) -> int:
    """Minimum Operations."""
    _primes: Set[int] = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                             43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                             101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
                             151, 157, 163, 167, 173, 179, 181, 192, 193, 197,
                             199, 211, 223, 227, 229])
    max_prime: int = 229
    if not isinstance(n, int):
        return 0
    if n < 2:
        return 0
    if n < 4:
        return n

    def prime_factor(num: int) -> int:
        """Find least prime factor of num."""
        if num in _primes:
            return num
        for prime in _primes:
            if num % prime == 0:
                return prime
        nonlocal max_prime
        if num < (max_prime * 3):
            return num
        tmp: int = max_prime + 1
        # get a multiple of 6 as prime numbers follow a pattern ( 6n ± 1 )
        while tmp % 6 != 0:
            tmp -= 1
        tmp -= 1
        # loop counter
        # uncommet for checking counter
        # count: int = 0
        while True:
            # uncomment for checking counter
            # count += 1
            if num % tmp == 0:
                tmp = prime_factor(tmp)
                break
            if num % (tmp + 2) == 0:
                tmp = prime_factor(tmp + 2)
                break
            if (tmp * tmp) > num:
                tmp = num
                break
            tmp += 6
            # uncomment for checking counter
            # print(f'iterated [{count}] times to get [{num}]')
        return tmp

    factors: List[int] = []
    tmp: int = n
    while True:
        factor = prime_factor(tmp)
        factors.append(factor)
        if factor == tmp:
            break
        tmp = int(tmp / factor)
    return int(sum(factors))
