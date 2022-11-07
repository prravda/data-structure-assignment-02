from unittest import TestCase
from mock_tree_dataset import mock_tree_dataset_two, TreeTestDataSet
from traverser import Traverser


class TestTraverserSetTwo(TestCase):
    def setUp(self) -> None:
        self.__test_case: TreeTestDataSet = mock_tree_dataset_two
        self.__traverser: Traverser = Traverser()

    def test_preorder(self):
        self.assertEqual(
            self.__test_case.expected_result_preorder,
            self.__traverser.preorder(self.__test_case.tree_data),
        )

    def test_inorder(self):
        self.assertEqual(
            self.__test_case.expected_result_inorder,
            self.__traverser.inorder(self.__test_case.tree_data),
        )

    def test_postorder(self):
        self.assertEqual(
            self.__test_case.expected_result_postorder,
            self.__traverser.postorder(self.__test_case.tree_data),
        )

    def test_breadth_first(self):
        self.assertEqual(
            self.__test_case.expected_result_breadth_first,
            self.__traverser.breadth_first(self.__test_case.tree_data),
        )
