from random import randint
from unittest import TestCase

from sort.quick import partition, quick_sort


def random_list(length=10, min_value=0, max_value=100):
    return [randint(min_value, max_value) for i in xrange(length)]


class PartitionTestCase(TestCase):
    def test_arranged_partition(self):
        values = range(10)
        pivot = 5
        partition(values, pivot, 0, len(values) - 1)
        self.assertEqual(values, range(10))

    def test_rearranged_partition(self):
        values = list(reversed(range(10)))
        pivot = 5
        partition(values, pivot, 0, len(values) - 1)
        self.assertEqual(values, range(10))

    def test_simple_partition(self):
        values = [4, 2, 3, 10]
        end = partition(values, 2, 0, 2)
        self.assertEqual(end, 0)
        self.assertEqual(values[0], 2)

    def test_stohastic_partition(self):
        length = 100
        num_tries = 1000

        for i in xrange(num_tries):
            arr = random_list(length=length)
            pivot = arr[randint(0, len(arr) - 1)]
            end = partition(arr, pivot, 0, len(arr) - 1)

            for i in xrange(0, end + 1):
                self.assertLessEqual(arr[i], pivot)
            for i in xrange(end + 1, len(arr) - 1):
                self.assertGreaterEqual(arr[i], pivot)


class QuickSortTestCase(TestCase):
    def test_simple_sort(self):
        values = [4, 3, 10, 2]
        quick_sort(values)
        self.assertEqual(values, [2, 3, 4, 10])

    def test_stohastic_sort(self):
        length = 100
        num_tries = 1000

        for i in xrange(num_tries):
            arr = random_list(length=length)
            quick_sort(arr)
            self.assertEqual(arr, sorted(arr))
