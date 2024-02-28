#!/usr/bin/python3
"""
efficiently find minimum number of coins
"""

def makeChange(coins, total):
    """
    calculates fewest number of coins needed to
    meet a total amount
    """
    if total <= 0:  # if amt is less that n or 0
        return 0
    minc = [0] + [float("inf")] * (total)
    for coin in coins:
        for p in range(coin, total + 1):
            minc[p] = min(minc[p], minc[p - coin] + 1)
    return minc[-1] if minc[-1] != float("inf") else -1
