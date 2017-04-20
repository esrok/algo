from unittest import TestCase

from graph import Graph, Node
from graph import OrientedEdge as Edge
from graph.scc import build_reversed_graph, get_finishing_times, \
    get_leaders, get_strongly_connected_components


class SCCTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = Graph()
        nodes = [Node(i) for i in xrange(9)]
        cls.nodes = nodes
        cls.graph.add_node(*nodes)
        cls.graph.add_edge(
            # first SCC
            Edge(nodes[5], nodes[8]),
            Edge(nodes[2], nodes[5]),
            Edge(nodes[8], nodes[2]),
            # second SCC
            Edge(nodes[7], nodes[4]),
            Edge(nodes[1], nodes[7]),
            Edge(nodes[4], nodes[1]),
            # third SCC
            Edge(nodes[3], nodes[6]),
            Edge(nodes[6], nodes[0]),
            Edge(nodes[0], nodes[3]),
            # connectors
            Edge(nodes[7], nodes[5]),
            Edge(nodes[8], nodes[6]),
        )

    def test_components(self):
        self.assertItemsEqual(
            get_strongly_connected_components(self.graph),
            [
                {self.nodes[2], self.nodes[5], self.nodes[8]},
                {self.nodes[1], self.nodes[4], self.nodes[7]},
                {self.nodes[0], self.nodes[3], self.nodes[6]},
            ]
        )
