from unittest import TestCase
from mock_tree_dataset import mock_tree_dataset_one, TreeTestDataSet
from utilities import Utilities


class TestUtilitiesSetOne(TestCase):
    def setUp(self) -> None:
        self.__test_case_set_one: TreeTestDataSet = mock_tree_dataset_one
        self.__utilities: Utilities = Utilities()

    def test_get_height_of_tree(self):
        self.assertEqual(
            self.__test_case_set_one.expected_result_height_of_tree,
            self.__utilities.get_height_of_tree(self.__test_case_set_one.tree_data),
        )

    def test_get_number_of_terminal_nodes(self):
        self.assertEqual(
            self.__test_case_set_one.expected_result_number_of_terminal_nodes,
            self.__utilities.get_number_of_terminal_nodes(self.__test_case_set_one.tree_data),
        )

    def test_get_number_of_nodes(self):
        self.assertEqual(
            self.__test_case_set_one.expected_result_number_of_total_nodes,
            self.__utilities.get_number_of_nodes(self.__test_case_set_one.tree_data),
        )
