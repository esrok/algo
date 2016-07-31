from unittest import TestCase

from npc.subset import pseudo_polynomial_subset


class PPSubsetTestCase(TestCase):
    def test_one_number_subset(self):
        numbers = [10]
        result = pseudo_polynomial_subset(numbers, 10)
        self.assertTrue(result)

    def test_none_number_subset(self):
        numbers = []
        result = pseudo_polynomial_subset(numbers)
        self.assertFalse(result)

    def test_simple_subset(self):
        numbers = [3, -1, -2, 10, -5, 11]
        result = pseudo_polynomial_subset(numbers)
        self.assertTrue(result)

    def test_min_sum_subset(self):
        numbers = [-3, -2, -1]
        result = pseudo_polynomial_subset(numbers, sum(numbers))
        self.assertTrue(result)

    def test_max_sum_subset(self):
        numbers = [1, 2, 3]
        result = pseudo_polynomial_subset(numbers, sum(numbers))
        self.assertTrue(result)
