"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        # TODO
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("the vertices do not exists in the graph")            

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # TODO
        # BFT Pseudocode
        # Create a queue
        queue = Queue()
        # Create list of visited nodes
        visited= set()
        # Put starting node in the queue
        queue.enqueue(starting_vertex)
        # While: queue not empty
        while queue.size()>0:
            # Pop first node out of queue
            vertex = queue.dequeue()
            # If not visited
            if vertex not in visited:
                #      Mark as visited
                visited.add(vertex)
                print(vertex)
                # Get adjacent edges and add to list
                for next_edge in self.vertices[vertex]:
                    queue.enqueue(next_edge)
            # Goto top of loop


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """        
        # TODO
        # Make a stack
        stack = Stack()
        # Add first node to stack
        stack.push(starting_vertex)
        # Make visited list
        visited= set()
        # While stack not empty:
        while stack.size() > 0:
            
            # print(f'\n stack is {stack.print_stack()} ')
            # Pop top item
            vertex = stack.pop()
            # if not visited:
            if vertex not in visited:
                # Mark as visited
                
                visited.add(vertex)
                print(f'dft vertex: {vertex}')
                # Get adjacent and add to stack
                for next_edge in self.vertices[vertex]:
                    stack.push(next_edge)

    def dft_recursive(self, starting_vertex,visited):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # TODO  
             
        visited.add(starting_vertex)
        print(starting_vertex) 
        for next_edge in self.vertices[starting_vertex]:
            if next_edge not in visited:
                self.dft_recursive(next_edge,visited)

#this code works too
    # def dft_recursive(self, starting_vertex,stack,visited):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.
    #     This should be done using recursion.
    #     """
    #     # TODO        
    #     stack.push(starting_vertex)
    #     if stack.size() > 0:
    #         vertex = stack.pop()
    #         if vertex not in visited:
    #             visited.add(vertex)
    #             print(vertex)
    #             for next_edge in self.vertices[vertex]:
    #                 self.dft_recursive(next_edge,stack,visited)



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        qq = Queue()
        visited = set()
        qq.enqueue([starting_vertex])

        while qq.size()>0:
            path = qq.dequeue()
            vertex = path[-1]

            if vertex not in visited:
                # Here is the point to so whetever we're trying to accomplish
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)


        # Still working on it
        # # TODO
        # array1=[]
        # prev=destination_vertex
        # for i in self.vertices:
        #     print(f'vertices i: {i} , {self.vertices[i]}')
        #     for j in self.vertices[i]:
        #         print(f'vertices {i} pointing to edge:{j}')
        #         if j == prev:
        #             array1.append(j)
        #     prev=i

        # print(f'array1 {array1}') 

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])

        while stack.size()>0:
            path = stack.pop()
            vertex = path[-1]

            if vertex not in visited:
                # Here is the point to so whetever we're trying to accomplish
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)


    #this code works too
    # def dfs(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.
    #     """
    #     # TODO
    #     stack = Stack()
    #     stack.push(starting_vertex)
    #     visited = set()
    #     while stack.size() >0 :
    #         vertex = stack.pop()
    #         if vertex not in visited:
    #             visited.add(vertex)
    #             print(vertex)
    #             if vertex == destination_vertex:
    #                 break
    #             for next_edge in self.vertices[vertex]:
    #                 stack.push(next_edge)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print('graph vertices')
    print(f'{graph.vertices} \n')

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('dft')
    graph.dft(1)
    print('\n')
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('bft')
    graph.bft(1)
    print('\n')
    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('dft recursive')
    # graph.dft_recursive(1,stack=Stack(),visited=set())
    graph.dft_recursive(1,visited=set())

    print('\n')

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('BFS')
    print(graph.bfs(1, 6))
    print('\n')

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('DFS')
    print(graph.dfs(1, 6))
