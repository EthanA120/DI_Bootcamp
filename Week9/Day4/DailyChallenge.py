# TASK: Binary Search Tree
class Node:
    """
        Polygons

        The goal of this exercise is to provide an OOP implementation of a binary search tree.
        Binary search tree

        In computer science, a tree is a data type that simulates a tree structure,
        with a root value and subtrees of children. Each node contains a value as seen in "Pic1.bmp".

        A binary search tree is a special type of tree (see "Pic2.bmp"), which respect the following properties:

            - Every node has at most two children
            - The left subtree of a node contains only nodes with keys lesser than the node’s key
            - The right subtree of a node contains only nodes with keys greater than the node’s key

        Part 1: The binary tree

            Let’s start by implementing a representation of a binary tree (a tree where every node has at most two children),
            a tree is represented by its root node.
            Create a class Node, it has three attributes, left, right and value,
            respectively its left and right child and its value, the children can be None.
            Then add the basic methods to this class:
            get_left(), get_right(), set_left(node), set_right(node), set_value(value) and get_value().


        Part 2: The binary search tree

            Now let’s transform this binary tree into a binary search tree,
            implement a function add_node(node) and add it to the three,
            make sure you respect all the conditions of the binary search tree (the node needs to be added at the right place,
            depending on its value).


        Part 3: Use the binary search tree
            Implement a method search(value) which return the node containing this value inside the tree.
    """

    # Create a node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Inorder traversal
def inorder(root):
    if root is not None:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.key) + "->", end=' ')
        # Traverse right
        inorder(root.right)


# Insert a node
def insert(node, key):
    # Return a new node if the tree is empty
    if node is None:
        return Node(key)
    # Traverse to the right place and insert the node
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


# Find the inorder successor
def min_value_node(node):
    current = node
    # Find the leftmost leaf
    while current.left is not None:
        current = current.left
    return current


# Deleting a node
def delete_node(root, key):
    # Return if the tree is empty
    if root is None:
        return root
    # Find the node to be deleted
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = min_value_node(root.right)
        root.key = temp.key
        # Delete the inorder successor
        root.right = delete_node(root.right, temp.key)
    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)
print("Inorder traversal: ", end=' ')
inorder(root)
print("\nDelete 10")
root = delete_node(root, 10)
print("Inorder traversal: ", end=' ')
inorder(root)
