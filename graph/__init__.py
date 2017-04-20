from collections import defaultdict
from itertools import chain
from Queue import LifoQueue


class Node(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Node %s' % self.value

    def __repr__(self):
        return self.__str__()


class Edge(object):
    def __init__(self, start, end, length=1):
        self.start = start
        self.end = end
        self.length = length

    def __eq__(self, other):
        return (
            self.start == other.start and
            self.end == other.end
        ) or (
            self.end == other.start and
            self.start == other.end
        )

    def __str__(self):
        return 'Edge %s <-> %s' % (self.start, self.end)

    def __repr__(self):
        return self.__str__()


class OrientedEdge(Edge):
    def __eq__(self, other):
        return (
            self.start == other.start and
            self.end == other.end
        )

    def __str__(self):
        return 'Edge %s -> %s' % (self.start, self.end)


class Graph(object):
    PRE_ORDER = 'in'
    POST_ORDER = 'post'

    def __init__(self):
        self._nodes = set()
        self._edges = defaultdict(set)

    def add_node(self, *nodes):
        for node in nodes:
            self._nodes.add(node)

    def add_edge(self, *edges):
        for edge in edges:
            assert edge.start in self._nodes
            assert edge.end in self._nodes
            self._edges[edge.start].add(edge)

    @property
    def nodes_count(self):
        return len(self._nodes)

    def iter_nodes(self):
        for node in self._nodes:
            yield node

    def iter_edges(self, start=None, end=None):
        if start is not None:
            edges = self._edges[start]
        else:
            edges = chain(*self._edges.itervalues())
        for edge in edges:
            if end is None or edge.end == end:
                yield edge

    def dfs(self, start_node, order=PRE_ORDER):
        current_path = LifoQueue()
        visited_nodes = set()
        current_path.put(start_node)

        while not current_path.empty():
            current_node = current_path.get()
            if current_node in visited_nodes:
                if order == self.POST_ORDER:
                    yield current_node
                continue
            else:
                visited_nodes.add(current_node)
                current_path.put(current_node)
            if order == self.PRE_ORDER:
                yield current_node
            for edge in self.iter_edges(start=current_node):
                if edge.end not in visited_nodes:
                    current_path.put(edge.end)
