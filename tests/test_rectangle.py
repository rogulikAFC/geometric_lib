import unittest

import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle.area(3, 5), 15)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(3, 5), 16)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-3, 5)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-3, 5)
