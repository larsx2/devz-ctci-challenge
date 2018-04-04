import unittest


class TestOneEdit(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(one_edit('pale', 'ple'))
        self.assertTrue(one_edit('pales', 'pale'))
        self.assertTrue(one_edit('pale', 'bale'))
        self.assertFalse(one_edit('pale', 'bake'))


def one_edit(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    else:
        return len(set(a).difference(set(b))) < 2
