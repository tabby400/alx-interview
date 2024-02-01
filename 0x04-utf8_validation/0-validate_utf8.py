#!/usr/bin/python3
"""
checking if a given set of data conforms to the rules
of UTF-8 encoding
"""


def validUTF8(data):
    """
    Returns True if data is a valid UTF-8 encoding
    otherwise False is returned
    """
    track_bytes = 0  # keep track of bytes rep a character
    for byte in data:  # iterate every byte in the data list
        if track_bytes == 0:  # if it is 0 shows start of a character
            if (byte >> 7) == 0b0:  # a 1 byte char
                track_bytes = 0
            elif (byte >> 5) == 0b110:  # a 2 byte char
                track_bytes = 1
            elif (byte >> 4) == 0b1110:  # a 3 byte char
                track_bytes = 2
            elif (byte >> 3 == 0b11110):  # 4 byte char
                track_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:  # checks if it is a continuation byte 10
                return False
            track_bytes = track_bytes - 1
    return track_bytes == 0  # all chars have been validated and encoded utf-8
