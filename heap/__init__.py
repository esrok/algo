
class Heap(object):
    def __init__(self, predicate):
        self._cmp = predicate
        self._keys = []

    def _swap(self, first, second):
        self._keys[first], self._keys[second] = \
            self._keys[second], self._keys[first]

    def _swift_up(self, index):
        current_index = index
        while current_index > 0:
            current_value = self._keys[current_index]
            parent_index = self._get_parent_index(current_index)
            parent_value = self._keys[parent_index]
            if not self._cmp(parent_value, current_value):
                self._swap(current_index, parent_index)
                current_index = parent_index
            else:
                break

    def _swift_down(self, index):
        current_index = index
        while not self._is_leaf(current_index):
            current_value = self._keys[current_index]
            left_child_index, right_child_index = self._get_child_indices(current_index)
            left_child_value = self._keys[left_child_index]

            min_index = left_child_index
            min_value = left_child_value
            if right_child_index is not None:
                right_child_value = self._keys[right_child_index]
                if not self._cmp(left_child_value, right_child_value):
                    min_index = right_child_index
                    min_value = right_child_value

            if not self._cmp(current_value, min_value):
                self._swap(current_index, min_index)
                current_index = min_index
            else:
                break

    def get(self):
        return self._keys[0]

    def extract(self):
        value = self._keys[0]
        self._swap(0, -1)
        self._keys.pop(-1)
        self._swift_down(0)
        return value

    def modify_key(self, old_value, new_value):
        pass

    def insert(self, key):
        self._keys.append(key)
        self._swift_up(len(self._keys) - 1)

    def _is_leaf(self, index):
        left_child_index, right_child_index = \
            self._get_child_indices(index)
        if left_child_index is None:
            return True
        return False

    def _get_parent_index(self, index):
        return (index - 1) / 2

    def _get_child_indices(self, index):
        left_index = index * 2 + 1
        if left_index >= len(self._keys):
            return None, None

        right_index = index * 2 + 2
        if right_index >= len(self._keys):
            return left_index, None
        return left_index, right_index


class MinHeap(Heap):
    def __init__(self, *elems):
        super(MinHeap, self).__init__(cmp=lambda x, y: x < y)


class MaxHeap(Heap):
    def __init__(self, *elems):
        super(MaxHeap, self).__init__(cmp=lambda x, y: x > y)
