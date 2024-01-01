from node import Node
from random import randint

def build_tree(node, low, high, vals_used):

    if not node:
        return node

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

def build_random_tree(node, num_nodes_in_tree, num_nodes_limit, vals_used):
    
    if not node or num_nodes_in_tree == num_nodes_limit:
        return node
    
    # Generate random values
    random_val_1 = randint(-50, 50)
    random_val_2 = randint(-50, 50)

    # Add values generated
    vals_used.add(random_val_1)
    vals_used.add(random_val_2)

    # Build left and right child nodes (Coinflip to generate left and right child)
    if randint(0, 1) == 0:
        node.left = build_random_tree(node = Node(val = random_val_1), num_nodes_in_tree = num_nodes_in_tree + 1, num_nodes_limit = num_nodes_limit, vals_used = vals_used)
    if randint(0, 1) == 1:
        node.right = build_random_tree(node = Node(val = random_val_2), num_nodes_in_tree = num_nodes_in_tree + 1, num_nodes_limit = num_nodes_limit, vals_used = vals_used)
    
    return node