#!/usr/bin/python3
"""module for minimum operations to get to a given number
of H's in a text file with only one H at the start"""


def minOperations(n):
    """
    fewest operations needed to get a specific value of n H's
    in a text file
    """
    #  n should atleast be more than two as we are copy pasting
    if (n < 2):
        return (0)  # n is impossible to achieve
    minoper, facn = 0, 2
    while facn <= n:  # factors of n to be used for copy paste
        #  find out if n is divisible by value of facn means
        #  facn is a factor of n and to be used in copy pasting
        if n % facn == 0:
            # if n is divible by facn if it is operations increase cp
            minoper = minoper + facn
            #  set n to the remainder
            n = n / facn  # n reps the remaining chars
            facn = facn - 1  # to find smaller factors to divide the updated n
        facn = facn + 1  # after looking at small facs it is incremented bignow
    return (minoper)
