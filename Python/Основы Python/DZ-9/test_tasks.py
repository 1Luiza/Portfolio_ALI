import unittest
from tasks import *


class TestsTasks(unittest.TestCase):

    def test_1(self):
        self.assertEqual(my_func(2, -3), 0.25)

    def test_2(self):
        self.assertNotEqual(my_func(2, -3), 10)

    def test_3(self):
        self.assertIn('winter', ['winter', 'spring', 'summer', 'autumn'])

    def test_4(self):
        self.assertNotIn('night', ['winter', 'spring', 'summer', 'autumn'])

    def test_5(self):
        self.assertIsInstance(Pen("ручкой"), Pen)

    def test_6(self):
        self.assertNotIsInstance(Pencil("карандашом"), Pen)

    def test_7(self):
        self.assertRaises(ZeroError, division, 3, 0)

    def test_8(self):
        self.assertEqual(division(6, 2), 3)

    def test_9(self):
        self.assertNotEqual(division(6, 2), 2)

    def test_10(self):
        self.assertIsNot(a, b)


if __name__ == '__main__':
    unittest.main()
