import unittest


class TestRotation(unittest.TestCase):

    def test_solution(self):
        s1 = "erbottlewat"
        s2 = "bottlewater"
        self.assertTrue(isSubstring(s2, s1 + s1))

        s1 = "barfoo"
        s2 = "foobar"
        self.assertTrue(isSubstring(s2, s1 + s1))

        s1 = "barfoo"
        s2 = "foobarbar"
        self.assertFalse(isSubstring(s2, s1 + s1))


def isSubstring(s1, s2):
    return s1 in s2
