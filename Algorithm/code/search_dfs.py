from collections import defaultdict
from collections import deque
import random


def dfs(node, graph, visited):
    if node in visited:
        return

    print(f'Visie: {node}')
    visited.add(node)

    for adjacent in graph[node]:
        dfs(adjacent, graph, visited)


if __name__ == "__main__":
    graph = defaultdict(set)

    n = random.randint(5, 10)
    for u in range(n):
        for v in range(n):
            threshold = random.random()
            if threshold >= 0.8:
                graph[u].add(v)
                graph[v].add(u)

    visitied = set()
    print(graph)
    dfs(0, graph, visitied)
