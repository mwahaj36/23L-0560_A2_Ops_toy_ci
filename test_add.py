import unittest


def add(a, b):
    return a + b


class AddTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 6)  # Intentional red run for CI demonstration.
