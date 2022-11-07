from mock_tree_dataset import mock_tree_dataset_one, mock_tree_dataset_two
from node import Node
from traverser import Traverser
from utilities import Utilities


def print_the_result_in_console(n: Node) -> None:
    traverser_instance = Traverser()
    utility_instance = Utilities()

    print("\n*** traverser testing ***\n")

    print(f"preorder:  {traverser_instance.preorder(n)}")
    print(f"inorder:  {traverser_instance.inorder(n)}")
    print(f"postorder:  {traverser_instance.postorder(n)}")
    print(f"level order:  {traverser_instance.breadth_first(n)}")

    print("\n*** utility testing ***\n")

    print(f"height of tree: {utility_instance.get_height_of_tree(n)}")
    print(f"number of terminal nodes: {utility_instance.get_number_of_terminal_nodes(n)}")
    print(f"number of total nodes: {utility_instance.get_number_of_nodes(n)}")

    print("\n*** fin ***\n")


print("****** 0. left side tree ******")
print_the_result_in_console(mock_tree_dataset_one.tree_data)

print("****** 1. right side tree ******")
print_the_result_in_console(mock_tree_dataset_two.tree_data)
