

class Node(object):
    def __init__(self):
        self._edges = {}

    @property
    def is_leaf(self):
        return len(self._edges) == 0

    def add(self, edge):
        self._edges[edge.value] = edge

    def get(self, value):
        assert value in self._edges
        return self._edges[value]

    def has_edge(self, value):
        return value in self._edges


class Edge(object):
    def __init__(self, value, source, dest=None):
        self.value = value
        self.source = source
        self.dest = dest

    def __str__(self):
        return 'edge %s' % self.value

    def __repr__(self):
        return self.__str__()


def add_pattern(root, pattern):
    current_node = root
    for char in pattern:
        if current_node.has_edge(char):
            edge = current_node.get(char)
            current_node = edge.dest
        else:
            new_node = Node()
            new_edge = Edge(char, source=current_node, dest=new_node)
            current_node.add(new_edge)
            current_node = new_node

    last_node = Node()
    last_edge = Edge(None, source=current_node, dest=last_node)
    current_node.add(last_edge)


def build_trie(patterns):
    root = Node()
    for pattern in patterns:
        add_pattern(root, pattern)
    return root


def match(node, text, start_index=0):
    current_node = node
    result = []
    for index in xrange(start_index, len(text)):
        char = text[index]
        if not current_node.has_edge(char):
            return

        edge = current_node.get(char)
        result.append(edge.value)

        current_node = edge.dest
        if current_node.has_edge(None):
            yield start_index, index


def search(text, patterns):
    root = build_trie(patterns)

    for index in xrange(0, len(text)):
        for result in match(root, text, index):
            yield result
