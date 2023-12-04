from graph.graph import Graph
from scheme.scheme import Scheme
from math import sqrt


def a_star(graph, start_v, end_v):
    def manhattan_distance(a_vertex, b_vertex):
        return abs(a_vertex.col - b_vertex.col) + abs(a_vertex.row - b_vertex.row)

    def euclidean_distance(a_vertex, b_vertex):
        return sqrt(abs(a_vertex.col - b_vertex.col) + abs(a_vertex.row - b_vertex.row))


    row_len, col_len = len(graph.vertices), len(graph.vertices[0])
    dist = [[[float('inf'), float('inf'), float('inf'), None] for _ in range(col_len)] for _ in range(row_len)]

    unvisited = []
    visited = []

    man_dist = manhattan_distance(start_v, end_v)
    dist[start_v.row][start_v.col] = [man_dist, 0, man_dist, None]
    unvisited.append(start_v)
    while unvisited:
        cur_v = min(unvisited, key=lambda x: dist[x.row][x.col][0])
        unvisited.remove(cur_v)
        visited.append(cur_v)

        if cur_v == end_v:
            break

        for neigh in graph.adjacency_list[cur_v.row][cur_v.col]:
            cur_vert_g_val = dist[cur_v.row][cur_v.col][1]
            cur_neigh_g_val = cur_vert_g_val + neigh.weight

            if neigh in (unvisited, visited) and cur_neigh_g_val < dist[neigh.row][neigh.col][1]:
                dist[neigh.row][neigh.col][3] = cur_v
                dist[neigh.row][neigh.col][1] = cur_neigh_g_val
                dist[neigh.row][neigh.col][0] = cur_neigh_g_val + dist[neigh.row][neigh.col][2]
            elif neigh not in unvisited and neigh not in visited:
                unvisited.append(neigh)
                dist[neigh.row][neigh.col][3] = cur_v
                dist[neigh.row][neigh.col][2] = manhattan_distance(neigh, end_v)
                dist[neigh.row][neigh.col][1] = cur_neigh_g_val
                dist[neigh.row][neigh.col][0] = cur_neigh_g_val + dist[neigh.row][neigh.col][2]

    return dist


def shortest_path(algorithm, graph, start_v, end_v):
    distances = algorithm(graph, start_v, end_v)
    path = [end_v]

    cur_v = end_v
    while distances[cur_v.row][cur_v.col][3] is not None:
        cur_v = distances[cur_v.row][cur_v.col][3]
        path.append(cur_v)

    return path


def print_shortest_path(graph, start_v, end_v):
    path = shortest_path(a_star, graph, start_v, end_v)

    for sublist in graph.vertices:
        for vertex in sublist:
            if vertex in path and vertex != start_v and vertex != end_v:
                print('.', end='')
            else:
                print(vertex.char, end='')
        print()


def print_alg_values(distances):
    for sublist in distances:
        for dist in sublist:
            if dist[0] == float('inf'):
                print('  ', end='\t')
            else:
                print(round(dist[0], 2), end='\t')
        print()


def main():
    graph = Graph(Scheme.num1)
    print_alg_values(a_star(graph, graph.get_vertex('R'), graph.get_vertex('C')))
    print_shortest_path(graph, graph.get_vertex('R'), graph.get_vertex('C'))
    graph.print_graph()


if __name__ == '__main__':
    main()
