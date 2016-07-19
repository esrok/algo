from unittest import TestCase

from heap import Heap


class HeapTestCase(TestCase):
    def setUp(self):
        self.values = [3, 1, 4, 2]
        self.heap = Heap(predicate=lambda x, y: x < y)

        for value in self.values:
            self.heap.insert(value)

    def test_sorted(self):
        results = []
        for value in self.values:
            results.append(self.heap.extract())

        self.assertEqual(results, sorted(self.values))

    def test_get(self):
        self.assertEqual(self.heap.get(), self.values[1])
