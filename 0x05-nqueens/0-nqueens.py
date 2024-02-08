#!/usr/bin/python3

"""
The NQueens puzzle involving placing Non attacking queens on a
N X N chessboard"""

import sys

if len(sys.argv) != 2:  # correct number of args given is checked
    print('Usage: nqueens N')
    exit(1)


try:
    N_value = int(sys.argv[1])  # checks N is an int
except ValueError:
    print('N must ba a number')
    exit(1)

if N_value < 4:  # N has to be equal to or greater than 4
    print('N must ba at least 4')
    exit(1)


def nqueens_solution(n):
    ''' this returns a list of all possible solutions '''
    if n == 0:  # current row
        return [[]]  # all queens are on the board
    recur_solution = nqueens_solution(n - 1)
    return [solution + [(n, k + 1)]
            for k in range(N_value)
            for solution in recur_solution
            if pass_queen((n, k + 1), solution)]


def is_attacking(square, queen):
    '''checks if a square is attacked by any queen'''
    (row1, col1) = square  # checks if the square and queen are in
    (row2, col2) = queen  # same row column or diagonal
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def pass_queen(sqr, queens):
    '''
    this checks if its safe to place a queen at a sqr
    considers the already placed queens
    '''
    for queen in queens:
        if is_attacking(sqr, queen):
            return False
    return True


for config in reversed(nqueens_solution(N_value)):  # goes in evry solution
    outcome = []  # for each solution a new list forms
    for x in [list(x) for x in config]:
        outcome.append([k - 1 for k in x])
    print(outcome)
