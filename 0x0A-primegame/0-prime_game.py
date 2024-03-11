#!/usr/bin/python3
"""
This is a Prime Number game between Ben and Maria
"""


def getMultiples(num, aim):
    """
    gets the multiples of a number in a list
    """
    for p in aim:
        if p % num == 0:
            aim.remove(p)
    return aim


def isPrime(k):
    """
    finds a prime number
    """
    if k == 1:
        return False
    for j in range(2, k):
        if k % j == 0:
            return False
    return True


def noandPrimes(n):
    """
    display set into prime numbers and non-prime numbers.
    """
    counter = 0
    aim = list(n)
    for h in range(1, len(aim) + 1):
        if isPrime(h):
            counter += 1
            aim.remove(h)
            aim = getMultiples(h, aim)
        else:
            pass
    return counter


def isWinner(x, nums):
    """
    Ben and Maria play a game with a set of consecutive integers
    starting from 1 to n, then take turns choosing a
    prime number from the set and removing that number and its
    multiples from the set.
    The player that cannot make a move loses the game.
    """

    players = {'Maria': 0, 'Ben': 0}
    setints = set()
    for elem in range(x):
        nums.sort()
        num = nums[elem]
        for p in range(1, num + 1):
            setints.add(p)
            if p == num + 1:
                break
        primcnt = noandPrimes(setints)

        if primcnt % 2 == 0:
            players['Ben'] += 1
        elif primcnt % 2 != 0:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
