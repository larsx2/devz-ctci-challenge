import unittest


def brute_force(s):
    S = len(s)
    for i in xrange(S):
        for j in xrange(S):
            if i == j:
                continue

            if s[i] == s[j]:
                return False

    return True


def sorting_solution(s):
    S = len(s)
    li = sorted(s)
    
    prev = None
    for i in xrange(S):
        if prev is None:
            prev = s[i]
            continue

        if prev == s[i]:
            return False
            
    return True


def set_solution(s):
    return len(s) == len(set(s))


class TestUniqueChars(unittest.TestCase):

    def test_brute_force_solution(self):
        self.assertTrue(brute_force("abcdef"))
        self.assertFalse(brute_force("abcdefa"))

    def test_sorting_solution(self):
        self.assertTrue(sorting_solution("abcdef"))
        self.assertFalse(sorting_solution("abcdefa"))

    def test_set_solution(self):
        self.assertTrue(set_solution("abcdef"))
        self.assertFalse(set_solution("abcdefa"))
