class Graph :
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def add_vertex(self, vertex) :
        if vertex < self.V :
            return

        self.V += 1
        for vertex in self.graph :
            vertex.append(0)
        self.graph.append([0 for column in range(self.V)])


    def get_edges(self) :
        edges = []
        for vertex in self.graph :
            for neighbour in self.graph[vertex] :
                edges.append((vertex, neighbour))
        return edges

    def add_edge(self, vertex1, vertex2, weight) :
        self.graph[vertex1][vertex2] = weight
        self.graph[vertex2][vertex1] = weight

    def get_weight(self, vertex1, vertex2) :
        return self.graph[vertex1][vertex2]


    def get_adjacency_matrix(self):
        return self.graph

    def get_adjacency_list(self) :
        adjacency_list = []
        for i in range(len(self.graph)) :
            adjacency_list.append([])
            for j in range(len(self.graph)) :
                if j in self.graph[i] :
                    adjacency_list[i].append(j)
        return adjacency_list

    def floydWarshall(self, matrix):
        dist = matrix
        for k in range(len(matrix)):
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist

if __name__ == "__main__" :
    graph = Graph(4)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 3, 10)
    graph.add_edge(1, 2, 3)
    graph.add_edge(2, 3, 1)
    graph.add_vertex(4)

    print(graph.get_adjacency_matrix())
    print(graph.get_adjacency_list())

