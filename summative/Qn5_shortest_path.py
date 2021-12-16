# Graph is represented using adj list
from __future__ import annotations

import sys
from heapq import heappush, heappop
from collections import defaultdict


def createAdjList(edges: list[list[int]]) -> dict[list[int]]:
    g = defaultdict(list)
    # loop over every edge and add it to g
    for (start, end, weight) in edges:
        # Undirected graph has edge from start to end and end to start
        g[start].append([end, weight])
        g[end].append([start, weight])
    return g


def shortestPath(n: int, edges: list[list[int]], startNode: int) -> list[int]:
    """
    shortestPath returns a list of min distance between startNode and all other nodes in giving graph
    TIME COMPLEXITY: O(E*log(V)) -> E is number of edges and V is the number of vertices. We loop over all the edges (E)
        and we use min heap as a priority queue to get the minimum distance vertex which costs O(LogV).
    SPACE COMPLEXITY: O(E + V) -> E is number of edges and V is the number of vertices for creating an adjacency list.
    """
    graph = createAdjList(edges)
    weights = [sys.maxsize] * (n + 1)
    # Set the final weight of the start vertex to 0
    weights[startNode] = 0
    # Add the start vertex to top of stack
    stack = [(startNode, 0)]
    # Create a set to keep track of previously seen vertices
    seen = set()

    while stack:
        # Get last vertex from the top of the heap
        node, weight = heappop(stack)
        # If obtained vertex not seen before
        if node not in seen:
            # Add vertex to set of seen vertices
            seen.add(node)
            # Loop over all vertices connected to the current vertex v
            for v, w in graph[node]:
                # Obtain the curr weight to reach vertex child_v
                currWeight = weights[v]
                # Compare the curr weight with the weight obtained from v parents + weight between child_v and v.
                if currWeight > weight + w:
                    weights[v] = weight + w
                    # Push the new updated vertex to heap
                    heappush(stack, (v, weight + w))

    # Update weight of unreachable vertices to -1
    return [-1 if weight == sys.maxsize else weight for weight in weights[1:]]


n = 5
graph = [[1, 2, 5], [1, 3, 15], [2, 3, 6], [3, 4, 2]]
s = 1
shortestPathWeights = shortestPath(n, graph, s)
for ind in range(len(shortestPathWeights)):
    print(f"Min weight from {1} to {ind + 1} = {shortestPathWeights[ind]}")
