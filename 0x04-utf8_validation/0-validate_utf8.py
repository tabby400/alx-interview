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
    track_bytes = 0  # tracks the remaining bytes to complete a char
    for byte in data:
        mask = 1 << 7  # sets up a mask leftmost bit set to 1
        if not track_bytes:  # if track bytes is 0 start of new char
            while byte & mask:  # the most significant bit is 1
                track_bytes += 1
                mask >>= 1
            if not track_bytes:  # if no next bit in the byte it continues
                continue
            if track_bytes == 1 or track_bytes > 4:
                return False  # if the number of bytes is valid
        else:
            if byte >> 6 != 0b10:  # if its a continuation byte
                return False
        track_bytes -= 1
    return track_bytes == 0
