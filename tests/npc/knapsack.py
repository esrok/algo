from unittest import TestCase

from npc.knapsack import pseudo_polynomial_knapsack


class PPKnapsackTestCase(TestCase):
    def test_one_item_knapsack(self):
        items = [(10, 20)]
        max_weight = 10
        result = pseudo_polynomial_knapsack(items, max_weight)
        self.assertEqual(result, 20)

    def test_empty_knapsack(self):
        items = [(10, 10)]
        max_weight = 5
        result = pseudo_polynomial_knapsack(items, max_weight)
        self.assertEqual(result, 0)

    def test_simple_knapscak(self):
        items = [
            (1, 3),
            (2, 7),
            (1, 5),
            (4, 7),
            (2, 9),
        ]
        max_weight = 4
        result = pseudo_polynomial_knapsack(items, max_weight)
        self.assertEqual(result, 17)
