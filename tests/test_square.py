import unittest

import square


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(5), 25)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            square.area(-5)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square.perimeter(-5)
