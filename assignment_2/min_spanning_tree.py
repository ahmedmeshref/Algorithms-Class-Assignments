# Problem: Find the cost of the min spanning in a giving graph using Prim's Algorithm
import sys


def costMinSpanningTree(graph, startingVertex):
    # Number of vertices in graph
    V = len(graph)
    # Total number of seen edges
    no_edge = 0
    # Seen contains indices of all seen vertices
    seen = {startingVertex - 1}
    total_cost = 0
    while no_edge < V - 1:
        minimum_edge_cost = sys.maxsize
        fromV, toV = 0, 0
        for vertex1 in seen:
            for vertex2 in range(V):
                # If vertex2 not seen before and there is an edge between vertex1 and vertex2
                if (vertex2 not in seen) and graph[vertex1][vertex2]:
                    if minimum_edge_cost > graph[vertex1][vertex2]:
                        minimum_edge_cost = graph[vertex1][vertex2]
                        fromV, toV = vertex1, vertex2
        print(str(fromV + 1) + " -> " + str(toV + 1) + " : " + str(graph[fromV][toV]))
        seen.add(toV)
        no_edge += 1
        total_cost += minimum_edge_cost
    return total_cost


# g = [[0, 19, 5, 0, 0],
#      [19, 0, 5, 9, 2],
#      [5, 5, 0, 1, 6],
#      [0, 9, 1, 0, 1],
#      [0, 2, 6, 1, 0]]
g1 = [[0, 28, 0, 0, 0, 10, 0],
     [28, 0, 16, 0, 0, 0, 14],
     [0, 16, 0, 12, 0, 0, 0],
     [0, 0, 12, 0, 22, 0, 18],
     [0, 0, 0, 22, 0, 25, 24],
     [10, 0, 0, 0, 25, 0, 0],
     [0, 14, 0, 18, 24, 0, 0]]
print(costMinSpanningTree(g1, 6))
