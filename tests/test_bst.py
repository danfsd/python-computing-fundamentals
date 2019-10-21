import io
import sys
import unittest


from binary_search_tree import BST, BSTNode


class TestBinarySearchTree(unittest.TestCase):
    def __prepareForConsoleOutput(self):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    def __getConsoleOutput(self):
        sys.stdout = sys.__stdout__
        return self.capturedOutput.getvalue().rstrip().lstrip()

    def __getTraversalTree(self):
        #               8
        #             /  \
        #           4     9
        #          / \
        #        1    5
        #              \
        #               6
        #                \
        #                 7
        bst = BST()
        bst.insert(8)
        bst.insert(4)
        bst.insert(9)
        bst.insert(1)
        bst.insert(5)
        bst.insert(6)
        bst.insert(7)
        return bst

    def test_empty_insertion(self):
        bst = BST()
        bst.insert(4)
        bst.insert(3)
        bst.insert(5)
        bst.insert(2)
        nodeTwo = bst.root.left.left
        self.assertEqual(2, nodeTwo.value)

    def test_inorder(self):
        self.__prepareForConsoleOutput()
        bst = self.__getTraversalTree()
        bst.inorder()
        expected = "1 4 5 6 7 8 9"
        actual = self.__getConsoleOutput()
        self.assertEqual(expected, actual)

    def test_preorder(self):
        self.__prepareForConsoleOutput()
        bst = self.__getTraversalTree()
        bst.preorder()
        expected = "8 4 1 5 6 7 9"
        actual = self.__getConsoleOutput()
        self.assertEqual(expected, actual)

    def test_postorder(self):
        self.__prepareForConsoleOutput()
        bst = self.__getTraversalTree()
        bst.postorder()
        expected = "1 7 6 5 4 9 8"
        actual = self.__getConsoleOutput()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
