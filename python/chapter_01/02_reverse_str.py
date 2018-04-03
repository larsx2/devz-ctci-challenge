import unittest

class TestReverse(unittest.TestCase):

    def test_solution(self):
        s = "Hello World!"
        rev = s[::-1]
        self.assertEqual(rev, reverse_in_place(s))
        self.assertEqual(rev, reverse_pythonic(s))
        self.assertEqual(rev, reverse_reversed(s))


def reverse_in_place(s):
    S = len(s)
    s = list(s)
    for i in xrange(S/2):
        s[i], s[S-i-1] = s[S-i-1], s[i]

    return ''.join(s)


def reverse_pythonic(s):
    return s[::-1]


def reverse_reversed(s):
    return ''.join(reversed(s))
