from collections import defaultdict

from graph import Graph
from graph import OrientedEdge as Edge


def build_reversed_graph(graph):
    reversed_graph = Graph()
    reversed_graph.add_node(*graph.iter_nodes())
    for edge in graph.iter_edges():
        reversed_edge = Edge(edge.end, edge.start)
        reversed_graph.add_edge(reversed_edge)
    return reversed_graph


def get_finishing_times(graph):
    node_to_time = {}

    current_time = 0
    for start_node in graph.iter_nodes():
        # start_node will be the first node in its dfs
        for node in graph.dfs(start_node, order=Graph.POST_ORDER):
            if node not in node_to_time:
                node_to_time[node] = current_time
                current_time += 1
    return node_to_time


def get_leaders(graph, finishing_times):
    leaders = {}
    nodes_count = graph.nodes_count
    time_to_node = {t: n for n, t in finishing_times.iteritems()}
    last_finishing_time = nodes_count - 1
    while len(leaders) < nodes_count and last_finishing_time >= 0:
        current_node = time_to_node[last_finishing_time]
        current_leader = last_finishing_time
        for node in graph.dfs(current_node):
            if node in leaders:
                continue
            leaders[node] = current_leader
            last_finishing_time -= 1
    return leaders


def get_strongly_connected_components(graph):
    reversed_graph = build_reversed_graph(graph)
    finishing_times = get_finishing_times(reversed_graph)
    leaders = get_leaders(graph, finishing_times)
    components = defaultdict(set)
    for node, leader in leaders.iteritems():
        components[leader].add(node)

    return components.itervalues()
