from node import Node


class Utilities:
    def get_height_of_tree(self, node: Node) -> int:
        if node is None:
            return 0

        height_left = self.get_height_of_tree(node.left)
        height_right = self.get_height_of_tree(node.right)

        return height_right + 1 if height_right > height_left else height_left + 1

    def get_number_of_terminal_nodes(self, node: Node) -> int:
        if node is None:
            return 0

        if node and node.left is None and node.right is None:
            return 1

        return self.get_number_of_terminal_nodes(node.left) + self.get_number_of_terminal_nodes(node.right)

    def get_number_of_nodes(self, node: Node) -> int:
        if node is None:
            return 0

        return 1 + self.get_number_of_nodes(node.left) + self.get_number_of_nodes(node.right)