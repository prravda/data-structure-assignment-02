from node import Node
from dataclasses import dataclass, field


# define a data class for testing
@dataclass
class TreeTestDataSet:
    tree_data: Node
    expected_result_preorder: list[str]
    expected_result_inorder: list[str]
    expected_result_postorder: list[str]
    expected_result_breadth_first: list[str]

    expected_result_number_of_total_nodes: int
    expected_result_number_of_terminal_nodes: int
    expected_result_height_of_tree: int


# create a left-side tree on based on 8-1
mock_tree_instance_one = Node('A', Node('B'), Node('C'))

mock_tree_instance_one.left.left = Node('D')

mock_tree_instance_one.right.left = Node('E', Node('G'), Node('H'))
mock_tree_instance_one.right.right = Node('F')

# create a right-side tree on based on 8-1
mock_tree_instance_two = Node('+', Node('*'), Node('E'))

mock_tree_instance_two.left.left = Node('*', Node('/'), Node('C'))
mock_tree_instance_two.left.right = Node('D')

mock_tree_instance_two.left.left.left.left = Node('A')
mock_tree_instance_two.left.left.left.right = Node('B')


# wiring up the test case and the expected cases
# into a single data class
mock_tree_dataset_one = TreeTestDataSet(
    tree_data=mock_tree_instance_one,
    expected_result_preorder=['A', 'B', 'D', 'C', 'E', 'G', 'H', 'F'],
    expected_result_inorder=['D', 'B', 'A', 'G', 'E', 'H', 'C', 'F'],
    expected_result_postorder=['D', 'B', 'G', 'H', 'E', 'F', 'C', 'A'],
    expected_result_breadth_first=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],

    expected_result_number_of_total_nodes=8,
    expected_result_number_of_terminal_nodes=4,
    expected_result_height_of_tree=4,
)

mock_tree_dataset_two = TreeTestDataSet(
    tree_data=mock_tree_instance_two,
    expected_result_preorder=['+', '*', '*', '/', 'A', 'B', 'C', 'D', 'E'],
    expected_result_inorder=['A', '/', 'B', '*', 'C', '*', 'D', '+', 'E'],
    expected_result_postorder=['A', 'B', '/', 'C', '*', 'D', '*', 'E', '+'],
    expected_result_breadth_first=['+', '*', 'E', '*', 'D', '/', 'C', 'A', 'B'],

    expected_result_number_of_total_nodes=9,
    expected_result_number_of_terminal_nodes=5,
    expected_result_height_of_tree=5,
)
