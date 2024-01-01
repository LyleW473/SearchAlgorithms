from tree import build_tree
from node import Node

def dfs(node, order):

    if not node:
        return node
    
    order.append(node.val)
    dfs(node.left, order = order)
    dfs(node.right, order = order)
    return order

my_tree = build_tree(0, node = Node(val = 5), low = 0, high = 10, vals_used = set([5]))
order = dfs(i = 0, node = my_tree, order = [])
print(f"Traversal order: {order}")