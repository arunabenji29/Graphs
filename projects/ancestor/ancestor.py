import sys
sys.path.append('../graph')

from graph import Graph
from util import Stack
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for i in ancestors:
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
    print(f'graph vertices: {graph.vertices}')

    for i in ancestors:
        graph.add_edge(i[1],i[0])
    print(f'graph vertices with edges: {graph.vertices}')

    stack = Stack()
    visited = set()
    stack.push([starting_node])
    new_path = []

    while stack.size() > 0:
        path = stack.pop()
        vertex = path[-1]
        if vertex not in visited:
            visited.add(vertex)
            if graph.vertices[starting_node] == set():
                return -1
            for next_vert in graph.vertices[vertex]:
                new_path = list(path)
                new_path.append(next_vert)
                print(f'for node: {starting_node}, new path: {new_path}')
                stack.push(new_path)
                print(new_path) 
    return new_path[-1]

#in class solution

# def earliest_ancestor(ancestors, starting_node):
#     # Build the graph
#     graph = Graph()
#     for pair in ancestors:
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])
#         # Build edges in reverse
#         graph.add_edge(pair[1], pair[0])
#     # Do a BFS (storing the path)
#     q = Queue()
#     q.enqueue([starting_node])
#     max_path_len = 1
#     earliest_ancestor = -1
#     while q.size() > 0:
#         path = q.dequeue()
#         v = path[-1]
#         # If the path is longer or equal and the value is smaller, or if the path is longer)
#         if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
#             earliest_ancestor = v
#             max_path_len = len(path)
#         for neighbor in graph.vertices[v]:
#             path_copy = list(path)
#             path_copy.append(neighbor)
#             q.enqueue(path_copy)
#     return earliest_ancestor

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors,3))
# earliest_ancestor(test_ancestors,10)