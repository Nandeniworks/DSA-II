
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if value < current.info:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.info, end=" ")
    inorder(root.right)


# create BST
tree = BinarySearchTree()

# insert values
values = [4, 2, 7, 1, 3, 6]

for value in values:
    tree.insert(value)

# display BST
inorder(tree.root)
