from random import randint


def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, start, end):
    if start < end:
        index = randint(start, end)
        value = arr[index]
        middle = (start + end) / 2
        arr[middle], arr[index] = arr[index], arr[middle]
        new_end = partition(arr, value, start, end)
        _quick_sort(arr, start, new_end)
        _quick_sort(arr, new_end + 1, end)


def partition(arr, pivot, left_index=None, right_index=None):
    length = len(arr)
    assert 0 <= left_index < length
    assert 0 <= right_index < length
    left_index -= 1
    right_index += 1
    while True:
        left_index += 1
        while arr[left_index] < pivot:
            left_index += 1

        right_index -= 1
        while arr[right_index] > pivot:
            right_index -= 1

        if left_index >= right_index:

            return right_index
        arr[left_index], arr[right_index] = \
            arr[right_index], arr[left_index]
