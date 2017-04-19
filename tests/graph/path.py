from unittest import TestCase

from graph import Edge, Graph, Node
from graph.path import dijkstras_shortest_path, reconstruct_path


class DijkstrasPathTestCase(TestCase):
    def test_single_node_path(self):
        g = Graph()
        a = Node('A')
        g.add_node(a)
        paths = dijkstras_shortest_path(g, a)
        self.assertEqual(len(paths), 1)
        self.assertEqual(paths[a], (None, 0))

    def test_single_edge_path(self):
        g = Graph()
        a = Node('A')
        b = Node('A')
        g.add_node(a, b)
        g.add_edge(Edge(a, b, length=1))
        paths = dijkstras_shortest_path(g, a, b)
        self.assertEqual(paths[b], (a, 1))

    def test_simple_path(self):
        NODE_COUNT = 5
        PATH_LENGTH = 1
        g = Graph()
        first_node = None
        previous_node = None
        for i in xrange(NODE_COUNT):
            node = Node(i)
            if first_node is None:
                first_node = node
            g.add_node(node)
            if previous_node is not None:
                g.add_edge(Edge(previous_node, node, PATH_LENGTH))
            previous_node = node
        paths = dijkstras_shortest_path(g, first_node, previous_node)
        self.assertIn(previous_node, paths)
        _, path_length = paths[previous_node]
        self.assertEqual(path_length, (NODE_COUNT - 1) * PATH_LENGTH)

    def test_shorter_path(self):
        # a -1-> b -5-> c
        # |             |
        # |6            |2
        # v             v
        # d -----1----> e
        g = Graph()
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        g.add_node(a, b, c, d, e)
        g.add_edge(
            Edge(a, b, 1),
            Edge(b, c, 5),
            Edge(c, e, 2),
            Edge(a, d, 6),
            Edge(d, e, 1),
        )
        paths = dijkstras_shortest_path(g, a, e)
        _, path_length = paths[e]
        self.assertEqual(path_length, 6 + 1)
