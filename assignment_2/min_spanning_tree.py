# Problem: Find the cost of the min spanning in a giving graph using Prim's Algorithm
import sys


def costMinSpanningTree(graph, startingVertex):
    currVertex = startingVertex - 1
    # Number of vertices in graph
    V = len(graph)
    minSpanningTree = []
    validEdges = []
    # Seen contains indices of all seen vertices
    seen = set()
    while len(minSpanningTree) < V - 1:
        # Add vertex to seen vertices
        seen.add(currVertex)
        minimumCostEdge = [None, None, sys.maxsize]
        # Get all valid edges from the currVertex
        for vertex2 in range(V):
            # if there is an edge and vertex was not seen before, add it edge in the list of valid edges
            if graph[currVertex][vertex2] != 0 and vertex2 not in seen:
                validEdges.append([currVertex, vertex2, graph[currVertex][vertex2]])

        # Calc edge with minimum cost in all valid edges
        for edge in validEdges:
            if edge[2] < minimumCostEdge[2]:
                minimumCostEdge = edge

        # Add edge to minSpanningTree
        minSpanningTree.append([minimumCostEdge[0] + 1, minimumCostEdge[1] + 1, minimumCostEdge[2]])
        # Remove edge from list of all valid edges
        validEdges.remove(minimumCostEdge)
        # Update curr vertex
        currVertex = minimumCostEdge[1]

    return minSpanningTree


g1 = [[0, 28, 0, 0, 0, 10, 0],
      [28, 0, 16, 0, 0, 0, 14],
      [0, 16, 0, 12, 0, 0, 0],
      [0, 0, 12, 0, 22, 0, 18],
      [0, 0, 0, 22, 0, 25, 24],
      [10, 0, 0, 0, 25, 0, 0],
      [0, 14, 0, 18, 24, 0, 0]]
print(costMinSpanningTree(g1, 6))
