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

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self):
        self.left = left

    def set_right(self):
        self.right = right

    def set_value(self):
        self.value = value

    def get_value(self):
        return self.value

def add_node(node):
    pass

def search(value):
    pass