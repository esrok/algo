from unittest import TestCase

from graph import Edge, Graph, Node


class GraphTestCase(TestCase):
    NODE_COUNT = 5

    def test_iter_nodes(self):
        g = Graph()
        nodes = [Node(i) for i in xrange(self.NODE_COUNT)]
        g.add_node(*nodes)
        self.assertItemsEqual(
            g.iter_nodes(),
            nodes,
        )

    def test_iter_edges(self):
        g = Graph()
        edges = []
        first_node = None
        previous_node = None
        for i in xrange(self.NODE_COUNT):
            node = Node(i)
            if first_node is None:
                first_node = node
            g.add_node(node)
            if previous_node is not None:
                edge = Edge(previous_node, node)
                edges.append(edge)
            previous_node = node
        g.add_edge(*edges)
        self.assertItemsEqual(
            g.iter_edges(),
            edges,
        )
