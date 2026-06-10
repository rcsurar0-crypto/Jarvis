import unittest
from finder import Finder

class TestFinder(unittest.TestCase):

    def test_finder_exists(self):
        finder = Finder()
        self.assertIsNotNone(finder)

if __name__ == "__main__":
    unittest.main()
