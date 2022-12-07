class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def get_adjacency_list(self):
        return self.__graph_dict

    def get_adjadency_matrix(self):
        vertices = self.vertices()
        matrix = [[0 for i in range(len(vertices))] for j in range(len(vertices))]
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if vertices[j] in self.__graph_dict[vertices[i]]:
                    matrix[i][j] = 1
        return matrix

# call
if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }

    graph = Graph(g)
    graph.add_vertex("z")
    graph.add_edge({"a","z"})

    print(graph.get_adjacency_list())
    print(graph.get_adjadency_matrix())
