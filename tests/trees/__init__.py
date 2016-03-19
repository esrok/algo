from unittest import TestCase

from trees import BinaryTreeNode, SearchTree


class SearchTreeTestCase(TestCase):
    def setUp(self):
        self.tree = SearchTree()
        self.values = [1, 7, 4, 2]
        for v in self.values:
            self.tree.add(BinaryTreeNode(v))

    def test_empty_add(self):
        tree = SearchTree()
        node = BinaryTreeNode(value=1)
        tree.add(node)
        self.assertEqual(tree.root, node)
        self.assertEqual(list(tree.traverse_left_to_right()), [1])

    def test_invariant(self):
        self.tree._check_invariant()

    def test_traverse_left_to_right(self):
        self.assertEqual(
            sorted(self.values),
            list(self.tree.traverse_left_to_right())
        )

    def test_search(self):
        self.assertEqual(
            self.tree.search(self.values[1]),
            self.values[1]
        )
        self.assertIsNone(self.tree.search(10))

    def test_remove(self):
        self.tree.remove(self.values[2])
        self.assertIsNone(self.tree.search(self.values[2]))
