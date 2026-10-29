import unittest
from parser import parse_limit

class Limits(unittest.TestCase):
    def test_default(self):
        self.assertEqual(parse_limit(None), 20)
    def test_zero(self):
        self.assertEqual(parse_limit(0), 0)
    def test_string_zero(self):
        self.assertEqual(parse_limit("0"), 0)
    def test_negative(self):
        with self.assertRaises(ValueError):
            parse_limit(-1)

if __name__ == "__main__":
    unittest.main()
