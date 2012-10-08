import unittest
from glob import glob

# HACK: Get doctest2 directory into system path
import sys
import os
sys.path.append(os.path.abspath('.'))
import doctest2

class TestRestFeatures (unittest.TestCase):
    def test_rst_files(self):
        for filename in glob('./tests/rst/*.rst'):
            filename = os.path.abspath(filename)
            failures, tests = doctest2.testfile(
                filename, module_relative=False, verbose=False)
            self.assertTrue(failures == 0)

