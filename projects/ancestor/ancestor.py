import sys
sys.path.append('../graph')

from graph import Graph
from util import Stack

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
        # print(f'while stack size: {stack.size()}')
        # print(f'stack {stack.print_stack()}')
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

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors,3))
# earliest_ancestor(test_ancestors,10)