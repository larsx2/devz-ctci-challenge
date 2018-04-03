import unittest


class TestCompress(unittest.TestCase):

    def test_normal(self):
        s = "abbcccdddd"
        self.assertEqual("a1b2c3d4", compress(s))

    def test_complex(self):
        s = "aaaabccccccccdaabcef"
        self.assertEqual("a4b1c8d1a2b1c1e1f1", compress(s))

    def test_short_bad(self):
        s = "a"
        self.assertEqual("a", compress(s))

    def test_bad(self):
        s = "abcdef"
        self.assertEqual("abcdef", compress(s))


def compress(s):
    S = len(s)
    result = []

    if S < 2:
        return s

    c = 1
    for i in xrange(S):

        # First pass
        if not result:
            result.append(s[i])
            continue

        if result[-1] == s[i]:
            c += 1
        else:
            result.append(str(c))
            result.append(s[i])
            c = 1

        # Last pass
        if S-1 == i:
            result.append(str(c))

        # Short-circuit if compression ends up bigger
        if S < len(result):
            return s

    return ''.join(result)
