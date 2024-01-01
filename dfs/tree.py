from node import Node

def build_tree(i, node, low, high, vals_used):

    if not node:
        return node

    # Left child
    if node.val > low and node.val - 1 not in vals_used:
        vals_used.add(node.val - 1)
        node.left = build_tree(i + 1, node = Node(val = node.val - 1), low = low, high = high, vals_used = vals_used)
        vals_used.remove(node.val - 1)
    # Right child
    if node.val < high and node.val + 1 not in vals_used:
        vals_used.add(node.val + 1)
        node.right = build_tree(i + 1, node = Node(val = node.val + 1), low = low, high = high, vals_used = vals_used)
        vals_used.remove(node.val + 1)
    
    return node