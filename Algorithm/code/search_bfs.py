from collections import defaultdict
from collections import deque
import random


def bfs(start, graph):
    n = len(graph)
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        print(f'Visit: {node}')

        for adjacent in graph[node]:
            if adjacent in visited:
                continue
            queue.append(adjacent)


if __name__ == "__main__":
    graph = defaultdict(set)

    n = random.randint(5, 10)
    for u in range(n):
        for v in range(n):
            threshold = random.random()
            if threshold >= 0.6:
                graph[u].add(v)
                graph[v].add(u)

    print(graph)
    bfs(0, graph)
