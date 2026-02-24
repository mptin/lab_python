from lab2 import guess_number, make_list
import unittest
    # Тесты
class TestMath(unittest.TestCase):
    def test_linear_easy(self):
        self.assertEqual(guess_number(1, 17, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), (17, 17))

    def test_linaer_more_diff(self):
        self.assertEqual(guess_number(1, 76, make_list([1, 15000])), (76, 76))

    def test_linear_negative(self):
        self.assertEqual(guess_number(1, -10, make_list([-10000, -1])), (-10, 9991))
