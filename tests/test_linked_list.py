import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_push(self):
        """
        Tests push operation on linked list.
        """
        list = LinkedList([2, 3, 4])
        pushedNode = list.push(1)
        self.assertEqual(pushedNode, list.head)

    def test_append(self):
        """
        Tests append operation on linked list.
        """
        list = LinkedList([1, 2, 3])
        appendedNode = list.append(4)
        self.assertEqual(appendedNode, list.tail)

    def test_nth_node(self):
        """
        Tests nth_node operation on linked list.
        """
        list = LinkedList()
        node = list.append(50)
        firstNode = list.nthNode(0)
        self.assertEqual(node, firstNode)

    def test_negative_nth_node(self):
        """
        Tests edge case on linked list's nth_node operation where the nth is a negative integer.
        """
        list = LinkedList([1, 2, 3])
        nthNode = list.nthNode(-1)
        self.assertIsNone(nthNode, "The nth node should be None")

    def test_out_of_bounds_nth_node(self):
        """
        Tests edge case on linked list's nth_node operation where the nth is a integer greater than the length of the list.
        """

    def test_length(self):
        """
        Tests the length operation on linked list.
        """
        list = LinkedList([1, 2, 3, 4, 5])
        listLength = list.getLength()
        self.assertEqual(5, listLength)

    def test_key_deletion(self):
        """
        Tests the deleteKey operation on linked list.
        """
        pass

    def test_delete_first_position(self):
        """
        Tests the delete position operation on linked list, deleting the first position.
        """
        list = LinkedList([1, 2, 3, 4])
        list.deletePosition(0)
        self.assertEqual(list.head.data, 2)

    def test_delete_last_position(self):
        """
        Tests the delete position operation on linked list, deleting the last position.
        """
        list = LinkedList([1, 2, 3, 4])
        list.deletePosition(3)
        self.assertEqual(list.tail.data, 3)

    def test_search(self):
        """
        Tests the search operation on linked list.
        """
        pass


if __name__ == "__main__":
    unittest.main()
