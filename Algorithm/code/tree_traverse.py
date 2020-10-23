from collections import defaultdict
import random


def traverse_preorder(node, tree):
    if node is None:
        return
    print(f'Visited(pre): {node}')
    traverse_preorder(tree[node]['left'], tree)
    traverse_preorder(tree[node]['right'], tree)


def traverse_inorder(node, tree):
    if node is None:
        return
    traverse_inorder(tree[node]['left'], tree)
    print(f'Visited(in): {node}')
    traverse_inorder(tree[node]['right'], tree)


def traverse_postorder(node, tree):
    if node is None:
        return
    traverse_postorder(tree[node]['left'], tree)
    traverse_postorder(tree[node]['right'], tree)
    print(f'Visited(post): {node}')


if __name__ == "__main__":
    tree = defaultdict(lambda: defaultdict(None))

    n = random.randint(5, 10)

    node = 0
    child_node = 1
    while node < n:
        tree[node]['left'] = None
        tree[node]['right'] = None

        if random.random() > 0.5:
            tree[node]['left'] = child_node
            child_node += 1
        if random.random() > 0.5:
            tree[node]['right'] = child_node
            child_node += 1

        node += 1

    while node < child_node:
        tree[node]['left'] = None
        tree[node]['right'] = None
        node += 1

    print(tree)
    traverse_preorder(0, tree)
    traverse_inorder(0, tree)
    traverse_postorder(0, tree)
