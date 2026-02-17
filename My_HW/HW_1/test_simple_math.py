import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):

    def setUp(self):

        self.math = SimpleMath()

    def test_square(self):

        self.assertEqual(self.math.square(4), 16)

        self.assertEqual(self.math.square(0), 0)

        self.assertEqual(self.math.square(-3), 9)

    def test_cube(self):

        self.assertEqual(self.math.cube(4), 64)

        self.assertEqual(self.math.cube(0), 0)

        self.assertEqual(self.math.cube(-3), -27)

if __name__ == '__main__':
    unittest.main()