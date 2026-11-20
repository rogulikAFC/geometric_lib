import unittest

import triangle


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle.area(3, 4), 6)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            triangle.area(-3, 4)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, 4, 5)

    def test_impossible_triangle(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 2, 10)
