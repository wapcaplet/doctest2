#!/usr/bin/env python

"""Run all tests.
"""

from glob import glob
import doctest2
import sys

def summarize(filename, statuses):
    print("=" * 30)
    print(filename)
    print("-" * 30)
    failures, tests = statuses
    print("%d tests, %d failures" % (tests, failures))
    print("=" * 30)
    print("")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-v':
        verbose = True
    else:
        verbose = False

    summarize('doctest2.py', doctest2.testmod(doctest2))
    for filename in glob('./tests/*.rst'):
        summarize(filename, doctest2.testfile(filename, verbose=verbose))

