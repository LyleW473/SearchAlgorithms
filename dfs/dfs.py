from tree import *
from node import Node
from random import seed as random_seed

def dfs(node, order):

    if not node:
        return node
    
    order.append(node.val)
    dfs(node.left, order = order)
    dfs(node.right, order = order)

tree1 = build_tree(node = Node(val = 5), low = 0, high = 10, vals_used = set([5]))
order1 = []
dfs(node = tree1, order = order1)
print(f"Traversal order 1: {order1}")

random_seed(2004)
tree2 = build_random_tree(node = Node(val = 5), num_nodes_in_tree = 0, num_nodes_limit = 20, vals_used = set([5]))
order2 = []
dfs(node = tree2, order = order2)
print(f"Traversal order 2: {order2}")