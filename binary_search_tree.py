
class BSTNode():

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value == self.value:
            print("Node is already on the BST")
            return False
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
                return True
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)
                return True

    def find(self, value):
        if value == self.value:
            return True
        elif value < self.value and self.left:
            return self.left.find(value)
        elif value > self.value and self.right:
            return self.right.find(value)
        else:
            return False

    def inorder(self):
        if self.left:
            self.left.inorder()

        print("% 2d" % self.value, end='')

        if self.right:
            self.right.inorder()

    def preorder(self):
        print("% 2d" % self.value, end='')

        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()

        print("% 2d" % self.value, end='')


class BST():

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return True

        return self.root.insert(value)

    def find(self, value):
        if self.root is None:
            return False
        elif self.root.value == value:
            return True
        else:
            return self.root.find(value)

    def inorder(self):
        if self.root is None:
            return
        self.root.inorder()

    def preorder(self):
        if self.root is None:
            return
        self.root.preorder()

    def postorder(self):
        if self.root is None:
            return
        self.root.postorder()
