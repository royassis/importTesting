import unittest
from importTesting.module_a import bar

class TestCase(unittest.TestCase):
    def test_bar(self):
        self.assertEqual(bar(1),1)