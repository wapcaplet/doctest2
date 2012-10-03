#!/usr/bin/env python

"""Run all tests.
"""

import doctest2

test_files = [
    'tests/ellipses.py',
]

if __name__ == '__main__':
    for filename in test_files:
        print("=" * 30)
        print(filename)
        print("=" * 30)

        doctest2.testfile(filename, verbose=True)

        print("")

