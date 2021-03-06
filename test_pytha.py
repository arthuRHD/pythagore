import unittest
from .pytha import pythagore

class TestPythagore(unittest.TestCase):
    """classe de test"""

    def test_theoreme(self):
        self.assertTrue(pythagore(5.0, 4.0, 3.0))
        self.assertFalse(pythagore(14.5, 5.8, 3.7))

    def test_type(self):
        self.assertRaises(AssertionError, pythagore, "5", 4, 3)
        self.assertRaises(AssertionError, pythagore, 2, 1, 0)
        self.assertRaises(AssertionError, pythagore, -2, 1, 1)
    
    def test_hypothenuse(self):
        self.assertRaises(AssertionError, pythagore, 1, 7, 7)