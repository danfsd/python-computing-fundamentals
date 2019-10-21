class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, array=None):
        self.head = None
        self.tail = None
        if array:
            for element in array:
                self.append(element)

    def push(self, new_data):
        # Creates new node
        new_node = Node(new_data)

        # Makes current head as new node's next
        new_node.next = self.head

        # Makes the head as the tail
        self.tail = self.head

        # Makes new node the current head
        self.head = new_node

        return new_node

    def insertAfter(self, prev_node, new_data):

        # Check whether the previous node is None
        if prev_node is None:
            print("The previous node is empty")
            return

        # Creating new node
        new_node = Node(new_data)

        # if prev_node.next is None:
        if prev_node == self.tail:
            # Makes the new node as the tail
            self.tail = new_node
        else:
            # Making the previous node's next as the new node's next
            new_node.next = prev_node.next

        # Making the new node as the previous node's next
        prev_node.next = new_node

        return new_node

    def append(self, new_data):

        # Create the new node
        new_node = Node(new_data)

        # If the Linked List is empty, makes new node as the head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return new_node

        self.tail.next = new_node
        self.tail = new_node

        return new_node

    def nthNode(self, position):
        if position >= self.getLength() or position < 0:
            print("The position % 2d is out of bounds" % position)
            return None

        count = 0
        current = self.head

        while (current):
            if count == position:
                return current
            count += 1
            current = current.next

    def getLength(self):
        length = 0
        current = self.head

        while (current):
            length += 1
            current = current.next

        return length

    def deletePosition(self, position):
        nth_node = self.nthNode(position)

        # If nth node is head, updates head
        if nth_node == self.head:
            self.head = nth_node.next
            return nth_node

        prev_node = self.nthNode(position - 1)

        if nth_node == self.tail:
            self.tail = prev_node

        prev_node.next = nth_node.next

        return nth_node

    def deleteKey(self, key):
        pass
