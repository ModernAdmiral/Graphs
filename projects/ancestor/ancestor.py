# Task: Search the given ancestor graph to the earliest one.

from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # create a graph out of ancestors
    graph = Graph()
    for x in range(1, 12):
        graph.add_vertex(x)
    for x in ancestors:
        # graph.add_edge(x[0], x[1])
        graph.add_edge(x[1], x[0])
    return graph.vertices


print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6),
                         (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 1))
