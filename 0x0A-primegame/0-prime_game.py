#!/usr/bin/python3
"""0x0A. Prime Game.

Algorithm
Python
"""
from typing import Set, List


def isWinner(x, nums):
    """Prime Game

    Maria and Ben are playing a game. Given a set of consecutive integers
    starting from 1 up to and including n, they take turns choosing a prime
    number from the set and removing that number and its multiples from the
    set. The player that cannot make a move loses the game.

    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is."""

    def prime_factors(num):
        """Get prime factors of a number"""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
                  151, 157, 163, 167, 173, 179, 181, 192, 193, 197,
                  199, 211, 223, 227, 229]
        max_prime = 229
        if not isinstance(num, int):
            return []
        if num <= max_prime:
            factors = []
            for n in primes:
                if n > num:
                    break
                factors.append(n)
            return factors

        def is_next_prime(num):
            """is prime checher."""
            for prime in primes:
                if num % prime == 0:
                    return False
            return True
 
        factors = list(primes)
        tmp = num
        while tmp % 6 != 0:
            tmp -= 1
        while tmp <= num:
            if is_next_prime(tmp - 1):
                factors.append(tmp - 1)
            if is_next_prime(tmp + 1):
                factors.append(tmp + 1)
            tmp += 6
        return factors

    score = 0
    for ind in range(x):
        factors = prime_factors(nums[ind])
        if len(factors) % 2 == 0:
            score -= 1
        else:
            score += 1
    if score > 0:
        return "Maria"
    elif score < 0:
        return "Ben"
    return None
