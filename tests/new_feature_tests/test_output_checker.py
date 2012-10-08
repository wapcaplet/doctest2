"""Unit tests for new features in the OutputChecker class.
"""

import unittest
import doctest2

class TestCheckOutput (unittest.TestCase):
    def setUp(self):
        self.checker = doctest2.OutputChecker()


class TestBlankline (TestCheckOutput):
    def test_accept_period_for_blankline(self):
        want = "red\n.\ngreen"
        got = "red\n\ngreen"
        result = self.checker.check_output(want, got, 0)
        self.assertTrue(result)

    def test_dont_accept_period_for_blankline(self):
        want = "red\n.\ngreen"
        got = "red\n\ngreen"
        result = self.checker.check_output(
            want, got, doctest2.DONT_ACCEPT_BLANKLINE)
        self.assertFalse(result)

    def test_literal_period(self):
        want = "red\n.\ngreen"
        got = "red\n.\ngreen"
        result = self.checker.check_output(
            want, got, doctest2.DONT_ACCEPT_BLANKLINE)
        self.assertTrue(result)

class TestEllipsis (TestCheckOutput):
    def test_ellipsis_match_all(self):
        want = "<...>"
        got = "red\ngreen\nblue"
        result = self.checker.check_output(
            want, got, doctest2.ELLIPSIS)
        self.assertTrue(result)

    def test_ellipsis_at_beginning(self):
        want = "<...>\ngreen\nblue\n"
        got = "red\ngreen\nblue\n"
        result = self.checker.check_output(
            want, got, doctest2.ELLIPSIS)
        self.assertTrue(result)

    def test_ellipsis_in_middle(self):
        want = "red\n<...>\nblue\n"
        got = "red\ngreen\nblue\n"
        result = self.checker.check_output(
            want, got, doctest2.ELLIPSIS)
        self.assertTrue(result)


if __name__ == '__main__':
    pass



