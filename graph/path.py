def reconstruct_path(paths, end):
    current_node = end
    path = []
    while current_node is not None:
        path.insert(-1, current_node)
        current_node, path_length = paths[current_node]
    return path


def get_closest_node(paths, visited):
    min_node = None
    min_length = None
    for node, (previous, length) in paths.iteritems():
        if node in visited:
            continue

        if min_node is None or length < min_length:
            min_node = node
            min_length = length
    return min_node


def dijkstras_shortest_path(graph, start, end=None):
    visited = set()
    paths = {
        start: (None, 0)
    }

    while len(visited) < graph.nodes_count:
        current_node = get_closest_node(paths, visited)
        if end is not None and current_node == end:
            break
        visited.add(current_node)
        previous_node, current_path = paths[current_node]

        for edge in graph.iter_edges(start=current_node):
            possible_path = current_path + edge.length
            current_end = edge.end
            _, current_end_path = paths.get(current_end, (None, None))

            if current_end_path is None or current_end_path > possible_path:
                paths[current_end] = (current_node, possible_path)
    return paths
