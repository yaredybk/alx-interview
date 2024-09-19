#!/usr/bin/python3
from typing import List
"""Change comes from within

Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of
    coin in the list
Your solution’s runtime will be evaluated in this task
"""


def makeChange(coins: List[int], total: int) -> int:
    """Find the fewest number of coins needed to meet a given total.

    this is the first iteration.
    just going from the highest coin to lowest
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    remainder = [0 for _ in coins]
    count = [0 for _ in coins]
    remaining = total

    for i, v in enumerate(coins):
        tmp_count = remaining // v
        if tmp_count == 0:
            continue
        remaining -= (tmp_count * v)
        remainder[i] = remaining
        count[i] = tmp_count
        if remaining == 0:
            break
    # print('rem\n', remainder)
    # print('count\n', count)
    if remaining > 0:
        return -1
    return sum(count)
