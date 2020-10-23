from collections import defaultdict
import heapq
import random


def get_parent(node, parents):
    if parents[node] == node:
        return node
    return get_parent(parents[node], parents)


def union_parent(u, v, parents):
    u_parent = get_parent(u, parents)
    v_parent = get_parent(v, parents)

    if u_parent < v_parent:
        parents[u] = u_parent
        parents[v] = u_parent
    elif v_parent > u_parent:
        parents[u] = v_parent
        parents[v] = v_parent


def kruskal_algorithm(graph):
    heap = list()
    visited = set()
    for u, adjacents in graph.items():
        for v, cost in adjacents.items():
            u, v = min(u, v), max(u, v)
            if (u, v) in visited:
                continue
            heapq.heappush(heap, (cost, u, v))
            visited.add((u, v))

    parents = {node: node for node in graph.keys()}
    total_cost = 0
    while heap:
        cost, u, v = heapq.heappop(heap)
        u_parent = get_parent(u, parents)
        v_parent = get_parent(v, parents)
        if u_parent == v_parent:
            continue
        union_parent(u, v, parents)
        total_cost += cost
        print(f'{u} -> {v}: {cost} / {total_cost}')


if __name__ == "__main__":
    graph = defaultdict(lambda: defaultdict(int))

    n = random.randint(5, 10)
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            threshold = random.random()
            if threshold >= 0.2:
                cost = random.randint(1, 100)
                graph[u][v] = cost
                graph[v][u] = cost

    print(graph)
    kruskal_algorithm(graph)
