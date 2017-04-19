class Node(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Node %s' % self.value

    def __repr__(self):
        return self.__str__()


class Edge(object):
    def __init__(self, start, end, length):
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
    def __init__(self):
        self._nodes = set()
        self._edges = set()

    def add_node(self, *nodes):
        for node in nodes:
            self._nodes.add(node)

    def add_edge(self, *edges):
        for edge in edges:
            assert edge.start in self._nodes
            assert edge.end in self._nodes
            self._edges.add(edge)

    @property
    def nodes_count(self):
        return len(self._nodes)

    def iter_nodes(self):
        for node in self._nodes:
            yield node

    def iter_edges(self, start=None, end=None):
        for edge in self._edges:
            if start is not None and edge.start != start:
                continue
            if end is not None and edge.end != end:
                continue
            yield edge
