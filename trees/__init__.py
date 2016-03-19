
class BinaryTreeNode(object):
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self._left = self._right = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        node.parent = self

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        node.parent = self

    def replace(self, new_node):
        if self.parent is None:
            return

        if self.parent.right == self:
            self.parent.right = new_node
        else:
            self.parent.left = new_node


class BinaryTree(object):
    PRE_ORDER = 'pre-order'
    IN_ORDER = 'in-order'
    POST_ORDER = 'post-order'

    TRAVERSE_TYPES = (PRE_ORDER, IN_ORDER, POST_ORDER)

    def __init__(self, root=None):
        self.root = root

    def add(self, node):
        raise NotImplementedError()

    def traverse_left_to_right(self):
        if self.root is None:
            return

        for node in self._traverse_left_to_right(self.root):
            yield node.value

    def _traverse_left_to_right(self, node, traverse_type=None):
        if traverse_type is None:
            traverse_type = self.IN_ORDER

        assert traverse_type in self.TRAVERSE_TYPES

        if traverse_type == self.PRE_ORDER:
            yield node
        if node.left is not None:
            for left_node in self._traverse_left_to_right(node.left):
                yield left_node

        if traverse_type == self.IN_ORDER:
            yield node

        if node.right is not None:
            for right_node in self._traverse_left_to_right(node.right):
                yield right_node
        if traverse_type == self.POST_ORDER:
            yield node


class SearchTree(BinaryTree):
    def get_path(self, node):
        parent = node.parent
        while parent is not None:
            yield parent
            parent = parent.parent

    def search_node(self, value):
        if self.root is None:
            return None

        current_node = self.root
        while True:
            if value > current_node.value:
                if current_node.right is None:
                    return None
                else:
                    current_node = current_node.right
            elif value < current_node.value:
                if current_node.left is None:
                    return None
                else:
                    current_node = current_node.left
            else:
                return current_node

    def search(self, value):
        result = self.search_node(value)
        if result is not None:
            return result.value

    def add(self, node):
        if self.root is None:
            self.root = node
            return

        current_node = self.root
        while True:
            if node.value > current_node.value:
                if current_node.right is None:
                    current_node.right = node
                    break
                else:
                    current_node = current_node.right
            elif node.value < current_node.value:
                if current_node.left is None:
                    current_node.left = node
                    break
                else:
                    current_node = current_node.left
            else:
                # values are equal
                # so no need to add
                break

    def _check_invariant(self):
        if self.root is None:
            return
        for node in self._traverse_left_to_right(self.root):
            if node.parent is None:
                continue
            if node == node.parent.left:
                assert node.value < node.parent.value
            else:
                assert node.value > node.parent.value

    def _successor(self, node):
        current_node = node

        if current_node.right is not None:
            return next(self._traverse_left_to_right(node.right))
        else:
            # child without right subtree
            while current_node is not None:
                parent = current_node.parent
                if parent is None:
                    # node has maximum value in tree
                    return None
                if parent.left == current_node:
                    # left child
                    return parent
                else:
                    # right child without right subtree
                    current_node = current_node.parent

    def remove(self, value):
        node = self.search_node(value)
        if node is None:
            raise Exception('trying to remove non-existing node')

        if node.right is None:
            # if node.left is None
            # node.parent.pointer will become None
            # and it is correct
            node.replace(node.left)
        elif node.left is None:
            node.replace(node.right)
        else:
            right = node.right
            left = node.left
            node.replace(right)
            right_left = next(self._traverse_left_to_right(right))
            right_left.left = left
        self._check_invariant()