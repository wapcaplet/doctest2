import unittest
import doctest2

class TestEllipsisMatch (unittest.TestCase):
    def test_no_ellipsis(self):
        result = doctest2._ellipsis_match("foo", "foo")
        self.assertTrue(result)

    def test_true_at_start(self):
        result = doctest2._ellipsis_match("...bar", "foobar")
        self.assertTrue(result)

    def test_false_at_start(self):
        result = doctest2._ellipsis_match("...bar", "foofoo")
        self.assertFalse(result)

    def test_true_in_middle(self):
        result = doctest2._ellipsis_match("aa...aa", "aaaa")
        self.assertTrue(result)

    def test_false_in_middle(self):
        result = doctest2._ellipsis_match("aa...aa", "aaa")
        self.assertFalse(result)

    def test_true_at_end(self):
        result = doctest2._ellipsis_match("foo...", "foobar")
        self.assertTrue(result)

    def test_false_at_end(self):
        result = doctest2._ellipsis_match("bar...", "foobar")
        self.assertFalse(result)


if __name__ == '__main__':
    pass

