import unittest
from calculator import add, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        # self.assertEqual(add(-1, 1), 0)
        # self.assertEqual(add(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 10)
            
if __name__ == '__main__':
    unittest.main()