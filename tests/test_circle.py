import unittest

import circle


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(1), 3.1415926536)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(1), 6.2831853072)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            circle.area(-1)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-1)
