from collections import defaultdict
from collections import deque
import random


def get_parent(node, parents):
    if parents[node] == node:
        return node
    return get_parent(parents[node], parents)


def union_parent(u, v, parents):
    u_parent = get_parent(u, parents)
    v_parent = get_parent(v, parents)

    if u_parent < v_parent:
        parents[v] = u_parent
    elif u_parent > v_parent:
        parents[u] = v_parent


if __name__ == "__main__":
    graph = defaultdict(set)

    n = random.randint(5, 10)
    for u in range(n):
        for v in range(n):
            threshold = random.random()
            if threshold >= 0.75:
                graph[u].add(v)
                graph[v].add(u)

    parents = {node: node for node in range(n)}
    print(graph)
    for u, adjacents in graph.items():
        for v in adjacents:
            union_parent(u, v, parents)

    print(parents)
