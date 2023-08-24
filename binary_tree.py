# a node has a value, and possibly two sons: left and/or right

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def construct_locally_complete_binary_tree(num_leaves):
    if num_leaves <= 0:
        return None

    root = Node(0)  # the root value is 0
    queue = [root]
    leaves_added = 1

    while leaves_added < num_leaves:
        current = queue.pop(0)

        # Add left child if there are still leaves to be added
        if leaves_added < num_leaves:
            current.left = Node(current.value * 2 + 1)
            queue.append(current.left)
            leaves_added += 1

        # Add right child if there are still leaves to be added
        if leaves_added < num_leaves:
            current.right = Node(current.value * 2 + 2)
            queue.append(current.right)
            leaves_added += 1

    return root


num_leaves = 8
root = construct_locally_complete_binary_tree(num_leaves)

# Traverse the tree in pre-order to display the structure


def traverse_preorder(node):
    if node is not None:
        print(node.value)
        traverse_preorder(node.left)
        traverse_preorder(node.right)


traverse_preorder(root)  # for 7 leaves, it prints 0 1 3 7 4 2 5 6

# to get the characteristics of the tree,


def get_external_nodes(node):
    if node is None:
        return []

    if node.left is None and node.right is None:
        return [node.value]

    external_nodes = []
    external_nodes.extend(get_external_nodes(node.left))
    external_nodes.extend(get_external_nodes(node.right))
    return external_nodes


def get_degree(node):
    if node is None:
        return 0

    degree = 0
    if node.left is not None:
        degree += 1
    if node.right is not None:
        degree += 1
    return degree


def get_levels(node):
    if node is None:
        return []

    queue = [(node, 1)]
    levels = []
    while queue:
        current, level = queue.pop(0)
        if level > len(levels):
            levels.append([])
        levels[level - 1].append(current.value)
        if current.left is not None:
            queue.append((current.left, level + 1))
        if current.right is not None:
            queue.append((current.right, level + 1))

    return levels


def get_height(node):
    if node is None:
        return 0

    left_height = get_height(node.left)
    right_height = get_height(node.right)
    return max(left_height, right_height) + 1


def get_path(node, target):
    if node is None:
        return None

    if node.value == target:
        return [node.value]

    left_path = get_path(node.left, target)
    if left_path is not None:
        return [node.value] + left_path

    right_path = get_path(node.right, target)
    if right_path is not None:
        return [node.value] + right_path

    return None


external_nodes = get_external_nodes(root)
degree = get_degree(root)
levels = get_levels(root)
height = get_height(root)
path = get_path(root, 5)

print("External Nodes:", external_nodes)  # la liste des feuilles
print("Degree:", degree)  # the maximum number of sons of a node in the tree
print("Levels:", levels)
print("Height:", height)
print("Path to 5:", path)


# add n nodes to a tree


def add_nodes(root, num_nodes):
    if root is None or num_nodes <= 0:
        return

    queue = [root]
    nodes_added = 0

    while nodes_added < num_nodes:
        current = queue.pop(0)

        if current.left is None:
            current.left = Node(current.value * 2 + 1)
            queue.append(current.left)
            nodes_added += 1

            if nodes_added == num_nodes:
                break

        if current.right is None:
            current.right = Node(current.value * 2 + 2)
            queue.append(current.right)
            nodes_added += 1

            if nodes_added == num_nodes:
                break

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)


# Add nodes to the previous tree
num_nodes_to_add = 3
add_nodes(root, num_nodes_to_add)

# Updated tree after adding nodes
print("Updated Tree:")
# Perform any necessary tree traversal to display the updated tree structure
traverse_preorder(root)
print("The characteristics of the tree are now")

external_nodes = get_external_nodes(root)
degree = get_degree(root)
levels = get_levels(root)
height = get_height(root)
path = get_path(root, 5)

print("External Nodes:", external_nodes)  # la liste des feuilles
print("Degree:", degree)  # the maximum number of sons of a node in the tree
print("Levels:", levels)
print("Height:", height)
print("Path to 5:", path)
