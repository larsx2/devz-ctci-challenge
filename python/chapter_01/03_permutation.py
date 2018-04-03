import unittest
import random


def randomize(s, as_list=False):
    l = list(s)
    random.shuffle(l)
    return l if as_list else ''.join(l)


class TestPermutation(unittest.TestCase):

    def test_solution(self):
        s = "abcdeff"

        for _ in xrange(100):
            self.assertTrue(is_permutation(s, randomize(s)))

        for _ in xrange(100):
            l = randomize(s, as_list=True)
            l.pop()
            self.assertFalse(is_permutation(s, ''.join(l)))


def is_permutation(a, b):
    return sorted(a) == sorted(b)
