from graph.graph import Graph
from scheme.scheme import Scheme
from math import sqrt


def a_star(graph, start_v, end_v):
    # f value -> g + h value - vertex with lowest f value is prioritized in traversal(visiting)
    #   --- it means that the current vertex could be(estimation/guess) the closest to the end vertex by air+ground ---
    # g value -> weights of all predecessor vertices + the weight of the current vertex
    # h value -> distance from current vertex to the end vertex (air distance - ignoring ground) (heuristic function)
    # predecessor -> visited neighbour vertex where that visited vertex's g value
    #   combined with the new g value of the current vertex is lower than the old g value of the current vertex
    #   --- They are used for being followed(bread crumbs) from end to start - similar to how the linked list works ---

    # manhattan_distance -> heuristic function
    #   -> how many x's and y's (not weights) it takes to traverse from the current point to the end point
    #   --- Better for this matrix representation ---
    def manhattan_distance(a_vertex, b_vertex):
        return abs(a_vertex.col - b_vertex.col) + abs(a_vertex.row - b_vertex.row)

    # euclidean_distance -> heuristic function -> pythagoras theorem from the current point to the end point
    #   --- Better for real world scenarios where the matrix is not as uniform in its shape and weights ---
    def euclidean_distance(a_vertex, b_vertex):
        return sqrt(abs(a_vertex.col - b_vertex.col) + abs(a_vertex.row - b_vertex.row))

    row_len, col_len = len(graph.vertices), len(graph.vertices[0])

    # dist = [f value, g value, h value, predecessor vertex] for each vertex
    # set the values to infinite for all vertices and set predecessor to None
    # Note: starting vertex will not have infinite values so that the algorithm can start from him
    dist = [[[float('inf'), float('inf'), float('inf'), None] for _ in range(col_len)] for _ in range(row_len)]
    unvisited = []
    visited = []

    man_dist = manhattan_distance(start_v, end_v)
    # Initialize the dist of the start vertex with non-infinite values
    dist[start_v.row][start_v.col] = [man_dist, 0, man_dist, None]
    # Append to unvisited vertices so that the algorithm begins from that point
    unvisited.append(start_v)
    # Do as long as there are unvisited vertices to visit
    while unvisited:
        # cur_v -> unvisited vertex with the smallest f value
        cur_v = min(unvisited, key=lambda x: dist[x.row][x.col][0])
        unvisited.remove(cur_v)
        # Append to visited, so it doesn't visit them again(add them to unvisited through neighbouring vertices)
        visited.append(cur_v)

        # if cur_v == end_v then the algorithm has visited the end vertex
        if cur_v == end_v:
            break

        # Update the values for each neighbour of the current vertex
        for neigh in graph.adjacency_list[cur_v.row][cur_v.col]:
            cur_vert_g_val = dist[cur_v.row][cur_v.col][1]
            cur_neigh_g_val = cur_vert_g_val + neigh.weight

            if neigh in (unvisited, visited) and cur_neigh_g_val < dist[neigh.row][neigh.col][1]:
                # If the neighbour is already in found(in unvisited) or visited
                # and his newly calculated g value is less than his old g value
                # then update(replace old with new) his g value and make his predecessor the current vertex

                dist[neigh.row][neigh.col][1] = cur_neigh_g_val
                dist[neigh.row][neigh.col][3] = cur_v
            elif neigh not in unvisited and neigh not in visited:
                # If the neighbour wasn't found, then add him to the unvisited list to be visited
                # Calculate all his values (f value, g value, h value) and set his predecessor

                unvisited.append(neigh)
                dist[neigh.row][neigh.col][3] = cur_v
                dist[neigh.row][neigh.col][2] = manhattan_distance(neigh, end_v)
                dist[neigh.row][neigh.col][1] = cur_neigh_g_val
                dist[neigh.row][neigh.col][0] = cur_neigh_g_val + dist[neigh.row][neigh.col][2]

    return dist


#  Add all predecessor vertices to a path list
def shortest_path(algorithm, graph, start_v, end_v):
    distances = algorithm(graph, start_v, end_v)
    path = [end_v]

    cur_v = end_v
    # Do while the predecessor is not None(start vertex has his predecessor set to None)
    while distances[cur_v.row][cur_v.col][3] is not None:
        cur_v = distances[cur_v.row][cur_v.col][3]
        path.append(cur_v)

    return path


# Print the graph/matrix with indexes of vertices found in path set to a chosen char(current(original) char set to '.')
def print_shortest_path(graph, start_v, end_v):
    path = shortest_path(a_star, graph, start_v, end_v)

    for sublist in graph.vertices:
        for vertex in sublist:
            # if vertex found in path (excluding starting and ending vertex - design choice - visibility)
            if vertex in path and vertex != start_v and vertex != end_v:
                print('.', end='')
            else:
                print(vertex.char, end='')
        print()


# Print the f values of all visited vertices by the algorithm (A* in this case)
def print_alg_values(distances):
    for sublist in distances:
        for dist in sublist:
            # infinite f value means that it has not been visited
            # (all f, g and h values of unvisited vertices are set to infinite)
            if dist[0] == float('inf'):
                # 'inf' makes the graph/matrix harder to read
                print('  ', end='\t')
            else:
                print(round(dist[0], 2), end='\t')
        print()


def main():
    graph = Graph(Scheme.num2)
    print_alg_values(a_star(graph, graph.get_vertex('R'), graph.get_vertex('C')))
    print_shortest_path(graph, graph.get_vertex('R'), graph.get_vertex('C'))
    graph.print_graph()


if __name__ == '__main__':
    main()
