import unittest

check_even_odd = __import__('dnaron task').check_even_odd
class TestEvenOdd(unittest.TestCase):

    def test_even_number(self):
        self.assertEqual(check_even_odd(4), '4 is even number')

    def test_odd_number(self):
        self.assertEqual(check_even_odd(7), '7 is an odd number.')

if __name__ == '__main__':
    unittest.main()