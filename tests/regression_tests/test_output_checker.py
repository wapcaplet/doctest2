"""Unit tests for regression-testing the OutputChecker class.
"""

import unittest
import doctest2

class TestCheckOutput (unittest.TestCase):
    def setUp(self):
        self.checker = doctest2.OutputChecker()


class TestExactMatch (TestCheckOutput):
    def test_match(self):
        want = "red\ngreen\nblue"
        got = want
        result = self.checker.check_output(want, got, 0)
        self.assertTrue(result)

    def test_no_match(self):
        want = "red\ngreen\nblue"
        got = "red\ngreenblue"
        result = self.checker.check_output(want, got, 0)
        self.assertFalse(result)


class TestNormalizedWhitespace (TestCheckOutput):
    def test_true_when_enabled(self):
        want = "['red',  'green',    'blue']"
        got = "['red', 'green', 'blue']"
        result = self.checker.check_output(
            want, got, doctest2.NORMALIZE_WHITESPACE)
        self.assertTrue(result)

    def test_false_when_disabled(self):
        want = "['red',  'green',    'blue']\n"
        got = "['red', 'green', 'blue']\n"
        result = self.checker.check_output(want, got, 0)
        self.assertFalse(result)


class TestBooleans (TestCheckOutput):
    def test_true_equals_1(self):
        want = "1\n"
        got = "True\n"
        result = self.checker.check_output(want, got, 0)
        self.assertTrue(result)

    def test_false_equals_0(self):
        want = "0\n"
        got = "False\n"
        result = self.checker.check_output(want, got, 0)
        self.assertTrue(result)


class TestDontAcceptTrueForOne (TestCheckOutput):
    def test_dont_accept_true_for_1(self):
        want = "1\n"
        got = "True\n"
        result = self.checker.check_output(
            want, got, doctest2.DONT_ACCEPT_TRUE_FOR_1)
        self.assertFalse(result)

    def test_dont_accept_false_for_0(self):
        want = "0\n"
        got = "False\n"
        result = self.checker.check_output(
            want, got, doctest2.DONT_ACCEPT_TRUE_FOR_1)
        self.assertFalse(result)


class TestBlankline (TestCheckOutput):
    def test_accept_blankline(self):
        want = "red\n<BLANKLINE>\ngreen"
        got = "red\n\ngreen"
        result = self.checker.check_output(want, got, 0)
        self.assertTrue(result)

    def test_accept_whitespace_as_blankline(self):
        want = "red\n<BLANKLINE>\ngreen"
        got = "red\n  \t  \ngreen"
        result = self.checker.check_output(want, got, 0)
        self.assertTrue(result)

    def test_dont_accept_blankline(self):
        want = "red\n<BLANKLINE>\ngreen"
        got = "red\n\ngreen"
        result = self.checker.check_output(
            want, got, doctest2.DONT_ACCEPT_BLANKLINE)
        self.assertFalse(result)

    def test_literal_blankline(self):
        want = "red\n<BLANKLINE>\ngreen"
        got = "red\n<BLANKLINE>\ngreen"
        result = self.checker.check_output(
            want, got, doctest2.DONT_ACCEPT_BLANKLINE)
        self.assertTrue(result)

class TestEllipsis (TestCheckOutput):
    def test_ellipsis_in_middle(self):
        want = "red\n...\nblue\n"
        got = "red\ngreen\nblue\n"
        result = self.checker.check_output(
            want, got, doctest2.ELLIPSIS)
        self.assertTrue(result)


class TestOutputDifference (unittest.TestCase):
    def setUp(self):
        self.checker = doctest2.OutputChecker()

    def test_something_equal(self):
        example = doctest2.Example("print(x)", "foo")
        result = self.checker.output_difference(example, "foo", 0)
        expected = "\n".join([
            "Expected:",
            "    foo",
            "Got:",
            "    foo",
        ])
        self.assertEqual(result, expected)

    def test_nothing_equal(self):
        example = doctest2.Example("print(x)", "")
        result = self.checker.output_difference(example, "", 0)
        expected = "\n".join([
            "Expected nothing",
            "Got nothing\n",
        ])
        self.assertEqual(result, expected)

    def test_simple_diff(self):
        example = doctest2.Example("print(x)", "foo")
        result = self.checker.output_difference(example, "bar", 0)
        expected = "\n".join([
            "Expected:",
            "    foo",
            "Got:",
            "    bar",
        ])
        self.assertEqual(result, expected)

    def test_want_something_got_nothing(self):
        example = doctest2.Example("print(x)", "foo")
        result = self.checker.output_difference(example, "", 0)
        expected = "\n".join([
            "Expected:",
            "    foo",
            "Got nothing\n",
        ])
        self.assertEqual(result, expected)

    def test_want_nothing_got_something(self):
        example = doctest2.Example("print(x)", "")
        result = self.checker.output_difference(example, "foo", 0)
        expected = "\n".join([
            "Expected nothing",
            "Got:",
            "    foo",
        ])
        self.assertEqual(result, expected)

    def test_got_blankline(self):
        example = doctest2.Example("print(x)", "foo\n<BLANKLINE>\nbar")
        result = self.checker.output_difference(example, "foo\n\nbar", 0)
        expected = "\n".join([
            "Expected:",
            "    foo",
            "    <BLANKLINE>",
            "    bar",
            "Got:",
            "    foo",
            "    <BLANKLINE>",
            "    bar",
        ])
        self.assertEqual(result, expected)

    def test_missing_blankline(self):
        example = doctest2.Example("print(x)", "foo\n<BLANKLINE>\nbar")
        result = self.checker.output_difference(example, "foo\nbar", 0)
        expected = "\n".join([
            "Expected:",
            "    foo",
            "    <BLANKLINE>",
            "    bar",
            "Got:",
            "    foo",
            "    bar",
        ])
        self.assertEqual(result, expected)


if __name__ == '__main__':
    pass


