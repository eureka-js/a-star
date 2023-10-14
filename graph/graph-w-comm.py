
class Vertex:
    # Node that represents each index in a graph/matrix
    def __init__(self, row, col, char, weight):
        self.char = char
        self.row = row
        self.col = col
        # self.weight -> instead of having edges for the sake of simplicity and not being needed for this representation
        #   This makes all the vertices equally distanced from their neighbours if they all have the same weight
        self.weight = weight


class Graph:
    # Representation of a matrix by vertices that hold multiple values(characteristics)

    def __init__(self, matrix):
        # Initialization of vertices and neighbors(adjacency_list) of each vertex
        self.vertices = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.adjacency_list = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        row_count = len(matrix)

        # Create a vertex at each index of vertices
        for row in range(row_count):
            for col in range(len(matrix[row])):
                char = matrix[row][col]
                match char:
                    case '#':
                        self.vertices[row][col] = Vertex(row, col, char, float('inf'))
                    case '|':
                        self.vertices[row][col] = Vertex(row, col, char, float('inf'))
                    case _:
                        self.vertices[row][col] = Vertex(row, col, char, 1)

        # Append a neighbour vertex at each index(index represents a list of neighbours for each vertex)
        # Can add diagonal neighbours as well if you want diagonal pathing
        for row in range(row_count):
            col_count = len(matrix[row])
            for col in range(col_count):
                if row > 0:
                    self.adjacency_list[row][col].append(self.vertices[row - 1][col])
                if row < row_count - 1:
                    self.adjacency_list[row][col].append(self.vertices[row + 1][col])
                if col > 0:
                    self.adjacency_list[row][col].append(self.vertices[row][col - 1])
                if col < col_count - 1:
                    self.adjacency_list[row][col].append(self.vertices[row][col + 1])
                """if row > 0 and col > 0:
                    self.adjacency_list[row][col].append(self.vertices[row - 1][col - 1])
                if row < row_count - 1 and col > 0:
                    self.adjacency_list[row][col].append(self.vertices[row + 1][col - 1])
                if col < col_count - 1 and row > 0:
                    self.adjacency_list[row][col].append(self.vertices[row - 1][col + 1])
                if row < row_count - 1 and col < col_count - 1:
                    self.adjacency_list[row][col].append(self.vertices[row + 1][col + 1])"""

    # Prints a representation of the graph with symbols
    def print_graph(self):
        for sublist in self.vertices:
            for vertex in sublist:
                print(vertex.char, end='')
            print()
        print()

    # Returns a vertex that represents a given char(symbol)
    def get_vertex(self, char):
        for sublist in self.vertices:
            for vertex in sublist:
                if vertex.char == char:
                    return vertex
