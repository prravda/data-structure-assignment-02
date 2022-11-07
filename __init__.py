from node import Node

# create a full-binary tree with Node class
mock_tree = Node(1, Node(2), Node(3))

mock_tree.left.left = Node(4)
mock_tree.left.right = Node(5)

mock_tree.right.left = Node(6)
mock_tree.right.right = Node(7)