from unittest import TestCase

from strings.trie import search, Node, Edge

class NodeTestCase(TestCase):
    def test_one_node(self):
        node = Node()
        self.assertTrue(node.is_leaf)

    def test_has_edge(self):
        root = Node()
        node = Node()
        value = 'c'
        edge = Edge(value, root, node)
        root.add(edge)
        self.assertTrue(root.has_edge(value))

    def test_get_edge(self):
        root = Node()
        node = Node()
        value = 'c'
        edge = Edge(value, root, node)
        root.add(edge)
        self.assertEqual(root.get(value), edge)


class TrieTestCase(TestCase):
    def test_equal_search(self):
        patterns = ['foobar']
        text = 'foobar'
        result = list(search(text, patterns))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], (0, len(text) - 1))

    def test_nonmatching_search(self):
        patterns = ['foobar']
        text = 'barfoo'
        result = search(text, patterns)
        self.assertIsNone(next(result, None))

    def test_simple_match(self):
        patterns = ['foo']
        text = 'foobarfoobar'
        result = list(search(text, patterns))
        self.assertEqual(result, [(0, 2), (6, 8)])

    def test_prefix_match(self):
        patterns = ['foo', 'foobar']
        text = 'bazfoobarbaz'

        result = list(search(text, patterns))
        self.assertEqual(result, [(3, 5), (3, 8)])
