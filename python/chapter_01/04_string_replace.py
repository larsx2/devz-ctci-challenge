import unittest


class TestReplace(unittest.TestCase):

    def test_hello_world(self):
        s = "Hello World!"
        self.assertEqual("Hello%20World!", space_replace(s))

    def test_hello(self):
        s = "  Hello  "
        self.assertEqual("%20%20Hello%20%20", space_replace(s))

    def test_world(self):
        s = "World    "
        self.assertEqual("World%20%20%20%20", space_replace(s))

    def test_all(self):
        s = " Hello  World    ! "
        self.assertEqual("%20Hello%20%20World%20%20%20%20!%20", space_replace(s))


def space_replace(s):
    return ''.join(c if c != ' ' else '%20' for c in list(s))
