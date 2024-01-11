#!/usr/bin/python3
"""
There isn number of locked boxes in front of you.
Each box numbered sequentially
from 0 to n - 1,each box may
contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """
     this method determines if all the boxes can be opened.
     returns true or fals
    """
    #  check if boxws are not empty and is a list
    if not boxes or type(boxes) is not list:
        return False

    openedbox = [0]  # keeps track of the opened ones
    for k in openedbox:
        for key in boxes[k]:
            if key not in openedbox and key < len(boxes):
                openedbox.append(key)
    if len(openedbox) == len(boxes):
        return True
    return False  # if not all boxes can be opened
