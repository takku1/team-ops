import unittest
from keymap import lookup


class Keymap(unittest.TestCase):
    def test_known_codes(self):
        self.assertEqual(lookup(0x47), 0x47)
        self.assertEqual(lookup(0x4D), 0x4D)

    def test_unknown_code(self):
        self.assertIsNone(lookup(0x99))

    def test_keymap_gap(self):
        # pins today's gap; do not edit until the investigation names the cause,
        # then the fix updates this pin.
        self.assertIsNone(lookup(0x4B))


if __name__ == "__main__":
    unittest.main()
