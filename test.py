#!/usr/bin/env python

"""Run all tests.
"""

from glob import glob
import doctest2

def summarize(filename, statuses):
    print("=" * 30)
    print(filename)
    print("-" * 30)
    failures, tests = statuses
    print("%d tests, %d failures" % (tests, failures))
    print("=" * 30)
    print("")

if __name__ == '__main__':
    summarize('doctest2.py', doctest2.testmod(doctest2))
    for filename in glob('./tests/*.py'):
        summarize(filename, doctest2.testfile(filename, verbose=False))

