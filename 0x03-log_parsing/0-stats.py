#!/usr/bin/python3
"""
Involves taking info generated as output from log files and
giving them as stdin to get the stats
"""

import sys

if __name__ == '__main__':

    count, sizeofile = 0, 0
    httpcode = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status = {p: 0 for p in httpcode}  # status codes as keys in dict val is 0

    def print_stats(status: dict, file_size: int) -> None:
        print("File size: {:d}".format(sizeofile))
        for p, i in sorted(status.items()):
            if i:
                print("{}: {}".format(p, i))

    try:
        for line in sys.stdin:
            count = count + 1
            info = line.split()
            try:
                status_code = info[-2]
                if status_code in status:
                    status[status_code] += 1
            except BaseException:
                pass
            try:
                sizeofile += int(info[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(status, sizeofile)
        print_stats(status, sizeofile)
    except KeyboardInterrupt:
        print_stats(status, sizeofile)
        raise
