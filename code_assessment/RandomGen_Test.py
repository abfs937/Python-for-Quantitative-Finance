import unittest
from code_assessment.RandomGen import RandomGen


class RandomGen_Test(unittest.TestCase):

    def setUp(self):
        self.rg = RandomGen()

# Test the random_nums list have 5 items
    def test_list_size_generate_random_nums_equal_to_5(self):
        self.assertEqual(len(self.rg.generate_random_nums()), 5)

# Test the probabilities list have 5 items
    def test_list_size_generate_probabilities_equal_to_5(self):
        self.assertEqual(len(self.rg.generate_probabilities()), 5)

# Test sum of the probabilities list equal to 1
    def test_sum_of_generate_probabilities_equal_to_1(self):
        self.assertEqual(sum(self.rg.generate_probabilities()), 1)

# Test there is no zero item in the probabilities list
    def test_no_zero_item_in_generate_probabilities(self):
        for i in self.rg.generate_probabilities():
            self.assertNotEqual(i, 0)

# Test there is no duplicate item in the random_nums list
    def test_no_duplicate_item_in_generate_random_nums(self):
        list1 = self.rg.generate_random_nums()
        self.assertEqual(len(list1), len(set(list1)))


if __name__ == '__main__':
    unittest.main()