import unittest
from lab1 import sumOfTwo

class TestMath(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(sumOfTwo([2, 7, 11, 15], 9), [0, 1])

    def test_ex2(self):
        self.assertEqual(sumOfTwo([3, 2, 4], 6), [1, 2])

    def test_ex3(self):
        self.assertEqual(sumOfTwo([3, 3], 6), [0, 1])

# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)