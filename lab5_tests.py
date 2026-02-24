import unittest
from lab5 import gen_bin_tree

class TestMath(unittest.TestCase):
    def test_2_1(self): self.assertEqual(gen_bin_tree(2, 1), {'root': 2})
    def test_2_3(self): self.assertEqual(gen_bin_tree(2, 3), {'root': 2, 'left': {'root': 6, 'left': {'root': 18}, 'right': {'root': 10}}, 'right': {'root': 6, 'left': {'root': 18}, 'right': {'root': 10}}})
    def test_2_5(self): self.assertEqual(gen_bin_tree(2, 5), {'root': 2, 'left': {'root': 6, 'left': {'root': 18, 'left': {'root': 54, 'left': {'root': 162}, 'right': {'root': 58}}, 'right': {'root': 22, 'left': {'root': 66}, 'right': {'root': 26}}}, 'right': {'root': 10, 'left': {'root': 30, 'left': {'root': 90}, 'right': {'root': 34}}, 'right': {'root': 14, 'left': {'root': 42}, 'right': {'root': 18}}}}, 'right': {'root': 6, 'left': {'root': 18, 'left': {'root': 54, 'left': {'root': 162}, 'right': {'root': 58}}, 'right': {'root': 22, 'left': {'root': 66}, 'right': {'root': 26}}}, 'right': {'root': 10, 'left': {'root': 30, 'left': {'root': 90}, 'right': {'root': 34}}, 'right': {'root': 14, 'left': {'root': 42}, 'right': {'root': 18}}}}})

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)