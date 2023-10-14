
class Vertex:
    def __init__(self, row, col, char, weight):
        self.char = char
        self.row = row
        self.col = col
        self.weight = weight


class Graph:
    def __init__(self, matrix):
        self.vertices = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.adjacency_list = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        row_count = len(matrix)

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

    def print_graph(self):
        for sublist in self.vertices:
            for vertex in sublist:
                print(vertex.char, end='')
            print()
        print()

    def get_vertex(self, char):
        for sublist in self.vertices:
            for vertex in sublist:
                if vertex.char == char:
                    return vertex
