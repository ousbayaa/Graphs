"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set ()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Nonexistent Vert")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()

        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:
            currentNode = q.dequeue()
            if currentNode not in visited:
                print(currentNode)

                visited.add(currentNode)
                for nextNode in self.get_neighbors(currentNode):
                    if nextNode not in visited:
                        q.enqueue(nextNode)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()

        visited = set()

        s.push(starting_vertex)

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print (v)

                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        visited.add(starting_vertex)
        print(starting_vertex)

        neighbors = self.get_neighbors(starting_vertex)

        while len(neighbors) > 0:
            for each in neighbors:
                if each not in visited:
                    self.dft_recursive(each, visited)
                else:
                    return

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        q = Queue()

        q.enqueue([starting_vertex])

        visited = set()

        while q.size() > 0:
            currentPath = q.dequeue()
            lastNode = currentPath[-1]
            if lastNode not in visited:
                if lastNode == destination_vertex:
                    return currentPath
                else:
                    visited.add(lastNode)
                    neighbors = self.get_neighbors(lastNode)
                    for neighbor in neighbors:
                        copy = currentPath[:]
                        copy.append(neighbor)
                        q.enqueue(copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        s = Stack()

        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            currentPath = s.pop()
            lastNode = currentPath[-1]
            if lastNode not in visited:
                if lastNode == destination_vertex:
                    return currentPath
                else:
                    visited.add(lastNode)
                    neighbors = self.get_neighbors(lastNode)
                    for neighbor in neighbors:
                        copy = currentPath[:]
                        copy.append(neighbor)
                        s.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=Stack(), visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        currentPath = path.pop()

        if currentPath == None:
            currentPath = [starting_vertex]
        if currentPath[-1] not in visited:
            visited.add(currentPath[-1])
            for neighbor in self.get_neighbors(currentPath[-1]):
                if neighbor == destination_vertex:
                    currentPath.append(neighbor)
                    return currentPath
                copy = currentPath.copy()

                copy.append(neighbor)

                path.push(copy)

            return self.dfs_recursive(starting_vertex, destination_vertex, path, visited)

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
    print(graph.vertices)

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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
