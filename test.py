#!/usr/bin/env python

"""Run all tests.
"""

import doctest2

test_files = [
    'tests/ellipses.py',
]

if __name__ == '__main__':
    # self-test
    print("=" * 30)
    print("doctest2.py")
    print("-" * 30)
    failures, tests = doctest2.testmod(doctest2)
    print("%d tests, %d failures" % (tests, failures))
    print("=" * 30)
    print("")

    for filename in test_files:
        print("=" * 30)
        print(filename)
        print("-" * 30)
        failures, tests = doctest2.testfile(filename, verbose=False)
        print("%d tests, %d failures" % (tests, failures))
        print("=" * 30)
        print("")

