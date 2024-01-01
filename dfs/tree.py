from node import Node

def build_tree(node, low, high, vals_used):

    if not node:
        return node

    print(node.val, low, high)
    # Left child
    if node.val > low and node.val - 1 not in vals_used:
        vals_used.add(node.val - 1)
        node.left = build_tree(node = Node(val = node.val - 1), low = low, high = high, vals_used = vals_used)
        vals_used.remove(node.val - 1)
    # Right child
    if node.val < high and node.val + 1 not in vals_used:
        vals_used.add(node.val + 1)
        node.right = build_tree(node = Node(val = node.val + 1), low = low, high = high, vals_used = vals_used)
        vals_used.remove(node.val + 1)
    
    return node
    
tree = build_tree(node = Node(val = 5), low = 0, high = 10, vals_used = set([5]))

print(tree.val)
print(tree.left.val)
print(tree.right.val)
print(tree.left.left.val)
print(tree.left.right.val if tree.left.right else "No node")
print(tree.right.left.val if tree.right.left else "No node")
print(tree.right.right.val)