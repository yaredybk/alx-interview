#!/usr/bin/python3
"""Log Parser"""
import sys


if __name__ == '__main__':
    file_size = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    def print_stats():
        """ Print statistics """
        tmp = f'File size: {file_size[0]}\n'
        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                tmp += '{}: {}\n'.format(key, status_codes[key])
        sys.stdout.write(tmp)
        sys.stdout.flush()

    def parse_line(line):
        """ Checks the line for matches """
        try:
            line = line[:-1]
            word = line.split(' ')
            # File size is last parameter on stdout
            file_size[0] += int(word[-1])
            # Status code comes before file size
            status_code = int(word[-2])
            # Move through dictionary of status codes
            if status_code in status_codes:
                status_codes[status_code] += 1
        except BaseException:
            pass

    linenum = 1
    try:
        for line in sys.stdin:
            parse_line(line)
            """ print after every 10 lines """
            if linenum % 10 == 0:
                print_stats()
            linenum += 1
    except KeyboardInterrupt:
        print_stats()
