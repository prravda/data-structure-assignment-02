from node import Node
from queue import Queue


class Traverser:

    def preorder(self, node: Node) -> list[str]:
        """
        preorder traversing's order: V/L/R

        :param node: node to traverse
        :return: a list of string which hold element's value with preorder
        """

        elements: list[str] = []

        def traverser(n: Node):
            if n is not None:
                elements.append(n.data)
                traverser(n.left)
                traverser(n.right)

        traverser(node)
        return elements

    def inorder(self, node: Node) -> list[str]:
        """
        inorder traversing's order: L/V/R

        :param node: node to traverse
        :return: a list of string which hold element's value with inorder
        """

        elements = []

        def traverser(n: Node):
            if n is not None:
                traverser(n.left)
                elements.append(n.data)
                traverser(n.right)

        traverser(node)
        return elements

    def postorder(self, node: Node) -> list[str]:
        """
        postorder traversing's order: L/R/V

        :param node: node to traverse
        :return: a list of string which hold element's value with postorder
        """

        elements: list[str] = []

        def traverser(n: Node):
            if n is not None:
                traverser(n.left)
                traverser(n.right)
                elements.append(n.data)

        traverser(node)
        return elements

    def breadth_first(self, node: Node) -> list[str]:
        """
        breadth-first searching (BFS) way traversing

        :param node: node to traverse
        :return: a list of string which hold element's value with postorder
        """
        job_queue: Queue[Node] = Queue()
        job_queue.put(node)

        result: list[str] = []

        while not job_queue.empty():
            current_node = job_queue.get()

            if current_node is not None:
                result.append(current_node.data)

                job_queue.put(current_node.left)
                job_queue.put(current_node.right)

        return result



